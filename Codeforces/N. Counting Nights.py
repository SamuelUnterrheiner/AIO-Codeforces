import javax.swing.*;
import java.awt.*;
import java.awt.geom.Point2D;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Random;

public class SoulNight extends JPanel implements ActionListener, KeyListener {
    // Game constants
    static final int TILE_SIZE = 32;
    static final int MAP_W = 60, MAP_H = 50;
    static final int VIEW_W = 25, VIEW_H = 19;
    static final int WIDTH = VIEW_W * TILE_SIZE, HEIGHT = VIEW_H * TILE_SIZE;
    static final int PLAYER_SIZE = 28, ENEMY_SIZE = 28, BULLET_SIZE = 8;

    // Terrain types
    static final int FLOOR = 0, WALL = 1, DOOR = 2, SPAWN = 3, BATTLE = 4, CHEST = 5, PORTAL = 6;
    static final Color[] TERRAIN_COLORS = {
        new Color(50, 50, 60),   // Floor
        new Color(80, 40, 20),   // Wall
        new Color(180, 120, 40), // Door
        new Color(180, 180, 255), // Spawn
        new Color(80, 80, 120),   // Battle
        new Color(200, 180, 80),  // Chest
        new Color(120, 0, 200)    // Portal
    };

    //<editor-fold desc="Weapon and Enemy Type Constants">
    // Weapon Types (50 total)
    static final int PISTOL=0, MAGNUM=1, UZI=2, RIFLE=3, SNIPER=4, SHOTGUN=5, SAWNOFF=6, FLAMETHROWER=7, ROCKET_LAUNCHER=8, GRENADE_LAUNCHER=9,
            LASER_PISTOL=10, LASER_RIFLE=11, PLASMA_GUN=12, RAILGUN=13, LIGHTNING_GUN=14, FIRE_STAFF=15, ICE_STAFF=16, EARTH_STAFF=17, DARK_STAFF=18, HOLY_STAFF=19,
            THROWING_KNIVES=20, SHURIKEN=21, CROSSBOW=22, REPEATER_CROSSBOW=23, BOW=24, POISON_BOW=25, MINIGUN=26, BUBBLE_GUN=27, MUSIC_GUN=28, VULCAN_CANNON=29,
            ALIEN_GUN=30, GAUSS_RIFLE=31, NEEDLER=32, BEAM_SWORD=33, CHAIN_GUN=34, BFG_9000=35, VOID_CANNON=36, SINGULARITY_GUN=37, STAR_DESTROYER=38, CHICKEN_GUN=39,
            POTATO_LAUNCHER=40, SWORD=41, SPEAR=42, AXE=43, HAMMER=44, KATANA=45, DUAL_PISTOLS=46, AKIMBO_UZIS=47, TRIPLE_SHOTGUN=48, QUAD_ROCKETS=49;

    // Enemy Types (20 total)
    static final int GOBLIN=0, SKELETON=1, SLIME=2, ORC=3, GHOST=4, BAT=5, SPIDER=6, ZOMBIE=7, WIZARD=8, GOLEM=9,
            DEMON=10, SHADOW_ASSASSIN=11, CYCLOPS=12, DRAGON_WHELP=13, NECROMANCER=14, MIMIC=15, ELEMENTAL=16, BEHOLDER=17, LICH=18, TITAN=19;
    //</editor-fold>

    // Game state
    Player player;
    int score = 0, level = 1;
    boolean gameOver = false;
    boolean portalActive = false;

    int[][] map = new int[MAP_H][MAP_W];
    List<Room> rooms = new ArrayList<>();
    List<Enemy> enemies = new ArrayList<>();
    List<Bullet> bullets = new ArrayList<>();
    List<GunPickup> gunPickups = new ArrayList<>();
    List<Particle> particles = new ArrayList<>();
    Point portalPos = null;

    Timer timer = new Timer(16, this); // Approx 60 FPS
    Random rand = new Random();
    static Map<Integer, Weapon> weaponData = new HashMap<>();
    static Map<Integer, EnemyData> enemyData = new HashMap<>();    public SoulNight() {
        setPreferredSize(new Dimension(WIDTH, HEIGHT));
        setBackground(Color.BLACK);
        setFocusable(true);
        addKeyListener(this);
        initializeData();
        startNewGame();
        timer.start();
    }

    private void startNewGame() {
        level = 1;
        score = 0;
        player = new Player(0, 0);
        startNewLevel();
    }

    private void startNewLevel() {
        enemies.clear();
        bullets.clear();
        gunPickups.clear();
        particles.clear();
        rooms.clear();
        portalActive = false;
        portalPos = null;
        gameOver = false;
        generateMap();
        placePlayerInSpawn();
        placeGuns();

        if (level == 1) {
            player.health = player.maxHealth;
            player.gunInventory[0] = PISTOL;
            player.gunInventory[1] = -1;
            player.selectedGun = 0;
        }
    }

    private void placePlayerInSpawn() {
        if (!rooms.isEmpty()) {
            Room spawnRoom = rooms.get(0);
            player.x = spawnRoom.getCenterX() * TILE_SIZE;
            player.y = spawnRoom.getCenterY() * TILE_SIZE;
        } else { // Fallback
            player.x = MAP_W / 2.0 * TILE_SIZE;
            player.y = MAP_H / 2.0 * TILE_SIZE;
        }
    }

    //<editor-fold desc="Map Generation">
    private void generateMap() {
        for (int y = 0; y < MAP_H; y++) {
            for (int x = 0; x < MAP_W; x++) {
                map[y][x] = WALL;
            }
        }

        rooms.clear();
        int maxRooms = 15;
        int minRoomSize = 6, maxRoomSize = 12;

        for (int i = 0; i < maxRooms; i++) {
            int w = rand.nextInt(maxRoomSize - minRoomSize + 1) + minRoomSize;
            int h = rand.nextInt(maxRoomSize - minRoomSize + 1) + minRoomSize;
            int x = rand.nextInt(MAP_W - w - 2) + 1;
            int y = rand.nextInt(MAP_H - h - 2) + 1;

            Room newRoom = new Room(x, y, w, h);
            boolean failed = false;
            for (Room otherRoom : rooms) {
                if (newRoom.intersects(otherRoom)) {
                    failed = true;
                    break;
                }
            }

            if (!failed) {
                createRoom(newRoom);
                if (!rooms.isEmpty()) {
                    Point newCenter = new Point(newRoom.getCenterX(), newRoom.getCenterY());
                    Point prevCenter = new Point(rooms.get(rooms.size() - 1).getCenterX(), rooms.get(rooms.size() - 1).getCenterY());
                    createCorridor(prevCenter, newCenter);
                }
                rooms.add(newRoom);
            }
        }
        // Set room types
        if (!rooms.isEmpty()) {
            rooms.get(0).type = SPAWN;
            for(int i = 1; i < rooms.size(); i++) {
                rooms.get(i).type = rand.nextDouble() < 0.2 ? CHEST : BATTLE;
                rooms.get(i).isCleared = false;
                rooms.get(i).isEngaged = false;
            }
        }
        // Update map tiles based on final room types
        for(Room room : rooms) {
            for (int y = room.y1; y < room.y2; y++) {
                for (int x = room.x1; x < room.x2; x++) {
                    map[y][x] = room.type;
                }
            }
        }
    }

    private void createRoom(Room room) {
        for (int y = room.y1; y < room.y2; y++) {
            for (int x = room.x1; x < room.x2; x++) {
                map[y][x] = FLOOR;
            }
        }
    }

    private void createCorridor(Point p1, Point p2) {
        int x = p1.x;
        int y = p1.y;

        if (rand.nextBoolean()) { // Horizontal then vertical
            while (x != p2.x) {
                for (int i = -1; i <= 1; i++)     //<editor-fold desc="Game Loop (actionPerformed)">
    @Override
    public void actionPerformed(ActionEvent e) {
        if (gameOver) {
            repaint();
            return;
        }
        player.update(this);
        handlePickups();
        updateBullets();
        updateEnemies();
        updateParticles();
        handleCollisions();
        checkRoomState();
        checkPortal();
        repaint();
    }
    //</editor-fold>

    //<editor-fold desc="Game Logic Sub-methods">
    private void handlePickups() {
        Iterator<GunPickup> git = gunPickups.iterator();
        while (git.hasNext()) {
            GunPickup gp = git.next();
            if (player.getBounds().intersects(new Rectangle((int)gp.x, (int)gp.y, TILE_SIZE, TILE_SIZE))) {
                player.pickupGun(gp.type, this);
                git.remove();
            }
        }
    }

    private void updateBullets() {
        Iterator<Bullet> bit = bullets.iterator();
        while (bit.hasNext()) {
            Bullet b = bit.next();
            b.update();
            if (b.lifetime <= 0 || !isPassable(b.x, b.y, b.size)) {
                createParticles(b.x, b.y, 3, b.hostile ? Color.PINK : Color.ORANGE, 1.5, 15);
                bit.remove();
            }
        }
    }

    private void updateEnemies() {
        for (Enemy enemy : enemies) {
            enemy.update(this);
        }
    }

    private void updateParticles() {
        particles.removeIf(p -> !p.update());
    }

    private void handleCollisions() {
        // Player bullet vs Enemy
        Iterator<Bullet> bit = bullets.iterator();
        while (bit.hasNext()) {
            Bullet b = bit.next();
            if (b.hostile) continue;
            Iterator<Enemy> eit = enemies.iterator();
            while (eit.hasNext()) {
                Enemy enemy = eit.next();
                if (b.getBounds().intersects(enemy.getBounds())) {
                    enemy.takeDamage(b.damage);
                    createParticles(b.x, b.y, 3, enemy.color.brighter(), 2.0, 20);
                    bit.remove();
                    if (enemy.health <= 0) {
                        score += enemyData.get(enemy.type).scoreValue;
                        createParticles(enemy.x + ENEMY_SIZE/2.0, enemy.y + ENEMY_SIZE/2.0, 20, enemy.color, 3.0, 40);
                        eit.remove();
                    }
                    break;
                }
            }
        }

        // Enemy bullet vs Player
        bit = bullets.iterator();
        while (bit.hasNext()) {
            Bullet b = bit.next();
            if (b.hostile && b.getBounds().intersects(player.getBounds())) {
                player.takeDamage(b.damage);
                createParticles(b.x, b.y, 5, Color.RED, 2.0, 25);
                bit.remove();
            }
        }
        // Enemy vs Player
        Iterator<Enemy> eit = enemies.iterator();
        while (eit.hasNext()) {
            Enemy enemy = eit.next();
            if (enemy.getBounds().intersects(player.getBounds())) {
                player.takeDamage(1);
                createParticles(enemy.x + ENEMY_SIZE/2.0, enemy.y + ENEMY_SIZE/2.0, 20, enemy.color, 3.0, 40);
                eit.remove();
            }
        }

        if (player.health <= 0) {
            gameOver = true;
        }
    }

    private void checkRoomState() {
        int playerTileX = (int)((player.x + player.size/2) / TILE_SIZE);
        int playerTileY = (int)((player.y + player.size/2) / TILE_SIZE);

        for (Room room : rooms) {
            if (room.contains(playerTileX, playerTileY) && room.type == BATTLE && !room.isCleared && !room.isEngaged) {
                room.isEngaged = true;
                spawnEnemiesInRoom(room);
            }
            if (room.isEngaged && !room.isCleared) {
                boolean allEnemiesInRoomDead = true;
                for (Enemy e : enemies) {
                    if (room.contains((int)(e.x / TILE_SIZE), (int)(e.y / TILE_SIZE))) {
                        allEnemiesInRoomDead = false;
                        break;
                    }
                }
                if (allEnemiesInRoomDead) {
                    room.isCleared = true;
                }
            }
        }
    }

    private void spawnEnemiesInRoom(Room room) {
        int enemyCount = 2 + rand.nextInt(3) + level;
        for (int i = 0; i < enemyCount; i++) {
            int ex = room.x1 + 1 + rand.nextInt(room.w - 2);
            int ey = room.y1 + 1 + rand.nextInt(room.h - 2);
            int enemyType = rand.nextInt(enemyData.size());
            enemies.add(new Enemy(ex * TILE_SIZE, ey * TILE_SIZE, enemyType));
        }
    }

    private void checkPortal() {
        boolean allBattleRoomsCleared = true;
        for (Room room : rooms) {
            if (room.type == BATTLE && !room.isCleared) {
                allBattleRoomsCleared = false;
                break;
            }
        }

        if (allBattleRoomsCleared && !portalActive) {
            portalActive = true;
            Room spawnRoom = rooms.get(0);
            portalPos = new Point(spawnRoom.getCenterX(), spawnRoom.getCenterY());
            map[portalPos.y][portalPos.x] = PORTAL;
        }

        if (portalActive && portalPos != null &&
            (int)((player.x + player.size/2) / TILE_SIZE) == portalPos.x && (int)((player.y + player.size/2) / TILE_SIZE) == portalPos.y) {
            level++;
            startNewLevel();
        }
    }

    public boolean isPassable(double x, double y, int size) {
        int tx1 = (int)((x - size/2.0) / TILE_SIZE);
        int ty1 = (int)((y - size/2.0) / TILE_SIZE);
        int tx2 = (int)((x + size/2.0) / TILE_SIZE);
        int ty2 = (int)((y + size/2.0) / TILE_SIZE);

        if (tx1 < 0 || ty1 < 0 || tx2 >= MAP_W || ty2 >= MAP_H) return false;

        return map[ty1][tx1] != WALL && map[ty1][tx2] != WALL && map[ty2][tx1] != WALL && map[ty2][tx2] != WALL;
    }

    public void createParticles(double x, double y, int count, Color color, double maxSpeed, int maxLifetime) {
        for (int i = 0; i < count; i++) {
            particles.add(new Particle(x, y, color, maxSpeed, maxLifetime));
        }
    }
    //</editor-fold>
for (int j = -1; j <= 1; j++) {
                    if (y + i > 0 && y + i < MAP_H - 1 && x + j > 0 && x + j < MAP_W - 1) map[y + i][x + j] = FLOOR;
                }
                x += (x < p2.x) ? 1 : -1;
            }
            while (y != p2.y) {
                for (int i = -1; i <= 1; i++) for (int j = -1; j <= 1; j++) {
                    if (y + i > 0 && y + i < MAP_H - 1 && x + j > 0 && x + j < MAP_W - 1) map[y + i][x + j] = FLOOR;
                }
                y += (y < p2.y) ? 1 : -1;
            }
        } else { // Vertical then horizontal
            while (y != p2.y) {
                for (int i = -1; i <= 1; i++) for (int j = -1; j <= 1; j++) {
                    if (y + i > 0 && y + i < MAP_H - 1 && x + j > 0 && x + j < MAP_W - 1) map[y + i][x + j] = FLOOR;
                }
                y += (y < p2.y) ? 1 : -1;
            }
            while (x != p2.x) {
                for (int i = -1; i <= 1; i++) for (int j = -1; j <= 1; j++) {
                    if (y + i > 0 && y + i < MAP_H - 1 && x + j > 0 && x + j < MAP_W - 1) map[y + i][x + j] = FLOOR;
                }
                x += (x < p2.x) ? 1 : -1;
            }
        }
        // Carve one last time at the destination to smooth out the corner
        for (int i = -1; i <= 1; i++) for (int j = -1; j <= 1; j++) {
            if (y + i > 0 && y + i < MAP_H - 1 && x + j > 0 && x + j < MAP_W - 1) map[y + i][x + j] = FLOOR;
        }
    }
    //</editor-fold>

    private void placeGuns() {
        gunPickups.clear();
        for (Room room : rooms) {
            if (room.type == CHEST) {
                int gunType = rand.nextInt(weaponData.size());
                gunPickups.add(new GunPickup(room.getCenterX() * TILE_SIZE, room.getCenterY() * TILE_SIZE, gunType));
            }
        }
    }

    //<editor-fold desc="Game Loop (actionPerformed)">
    @Override
    public void actionPerformed(ActionEvent e) {
        if (gameOver) {
            repaint();
            return;
        }
        player.update(this);
        handlePickups();
        updateBullets();
        updateEnemies();
        updateParticles();
        handleCollisions();
        checkRoomState();
        checkPortal();
        repaint();
    }
    //</editor-fold>

    //<editor-fold desc="Game Logic Sub-methods">
    private void handlePickups() {
        Iterator<GunPickup> git = gunPickups.iterator();
        while (git.hasNext()) {
            GunPickup gp = git.next();
            if (player.getBounds().intersects(new Rectangle((int)gp.x, (int)gp.y, TILE_SIZE, TILE_SIZE))) {
                player.pickupGun(gp.type, this);
                git.remove();
            }
        }
    }

    private void updateBullets() {
        Iterator<Bullet> bit = bullets.iterator();
        while (bit.hasNext()) {
            Bullet b = bit.next();
            b.update();
            if (b.lifetime <= 0 || !isPassable(b.x, b.y, b.size)) {
                createParticles(b.x, b.y, 3, b.hostile ? Color.PINK : Color.ORANGE, 1.5, 15);
                bit.remove();
            }
        }
    }

    private void updateEnemies() {
        for (Enemy enemy : enemies) {
            enemy.update(this);
        }
    }

    private void updateParticles() {
        particles.removeIf(p -> !p.update());
    }

    private void handleCollisions() {
        // Player bullet vs Enemy
        Iterator<Bullet> bit = bullets.iterator();
        while (bit.hasNext()) {
            Bullet b = bit.next();
            if (b.hostile) continue;
            Iterator<Enemy> eit = enemies.iterator();
            while (eit.hasNext()) {
                Enemy enemy = eit.next();
                if (b.getBounds().intersects(enemy.getBounds())) {
                    enemy.takeDamage(b.damage);
                    createParticles(b.x, b.y, 3, enemy.color.brighter(), 2.0, 20);
                    bit.remove();
                    if (enemy.health <= 0) {
                        score += enemyData.get(enemy.type).scoreValue;
                        createParticles(enemy.x + ENEMY_SIZE/2.0, enemy.y + ENEMY_SIZE/2.0, 20, enemy.color, 3.0, 40);
                        eit.remove();
                    }
                    break;
                }
            }
        }

        // Enemy bullet vs Player
        bit = bullets.iterator();
        while (bit.hasNext()) {
            Bullet b = bit.next();
            if (b.hostile && b.getBounds().intersects(player.getBounds())) {
                player.takeDamage(b.damage);
                createParticles(b.x, b.y, 5, Color.RED, 2.0, 25);
                bit.remove();
            }
        }
        // Enemy vs Player
        Iterator<Enemy> eit = enemies.iterator();
        while (eit.hasNext()) {
            Enemy enemy = eit.next();
            if (enemy.getBounds().intersects(player.getBounds())) {
                player.takeDamage(1);
                createParticles(enemy.x + ENEMY_SIZE/2.0, enemy.y + ENEMY_SIZE/2.0, 20, enemy.color, 3.0, 40);
                eit.remove();
            }
        }

        if (player.health <= 0) {
            gameOver = true;
        }
    }

    private void checkRoomState() {
        int playerTileX = (int)((player.x + player.size/2) / TILE_SIZE);
        int playerTileY = (int)((player.y + player.size/2) / TILE_SIZE);

        for (Room room : rooms) {
            if (room.contains(playerTileX, playerTileY) && room.type == BATTLE && !room.isCleared && !room.isEngaged) {
                room.isEngaged = true;
                spawnEnemiesInRoom(room);
            }
            if (room.isEngaged && !room.isCleared) {
                boolean allEnemiesInRoomDead = true;
                for (Enemy e : enemies) {
                    if (room.contains((int)(e.x / TILE_SIZE), (int)(e.y / TILE_SIZE))) {
                        allEnemiesInRoomDead = false;
                        break;
                    }
                }
                if (allEnemiesInRoomDead) {
                    room.isCleared = true;
                }
            }
        }
    }

    private void spawnEnemiesInRoom(Room room) {
        int enemyCount = 2 + rand.nextInt(3) + level;
        for (int i = 0; i < enemyCount; i++) {
            int ex = room.x1 + 1 + rand.nextInt(room.w - 2);
            int ey = room.y1 + 1 + rand.nextInt(room.h - 2);
            int enemyType = rand.nextInt(enemyData.size());
            enemies.add(new Enemy(ex * TILE_SIZE, ey * TILE_SIZE, enemyType));
        }
    }

    private void checkPortal() {
        boolean allBattleRoomsCleared = true;
        for (Room room : rooms) {
            if (room.type == BATTLE && !room.isCleared) {
                allBattleRoomsCleared = false;
                break;
            }
        }

        if (allBattleRoomsCleared && !portalActive) {
            portalActive = true;
            Room spawnRoom = rooms.get(0);
            portalPos = new Point(spawnRoom.getCenterX(), spawnRoom.getCenterY());
            map[portalPos.y][portalPos.x] = PORTAL;
        }

        if (portalActive && portalPos != null &&
            (int)((player.x + player.size/2) / TILE_SIZE) == portalPos.x && (int)((player.y + player.size/2) / TILE_SIZE) == portalPos.y) {
            level++;
            startNewLevel();
        }
    }

    public boolean isPassable(double x, double y, int size) {
        int tx1 = (int)((x - size/2.0) / TILE_SIZE);
        int ty1 = (int)((y - size/2.0) / TILE_SIZE);
        int tx2 = (int)((x + size/2.0) / TILE_SIZE);
        int ty2 = (int)((y + size/2.0) / TILE_SIZE);

        if (tx1 < 0 || ty1 < 0 || tx2 >= MAP_W || ty2 >= MAP_H) return false;

        return map[ty1][tx1] != WALL && map[ty1][tx2] != WALL && map[ty2][tx1] != WALL && map[ty2][tx2] != WALL;
    }

    public void createParticles(double x, double y, int count, Color color, double maxSpeed, int maxLifetime) {
        for (int i = 0; i < count; i++) {
            particles.add(new Particle(x, y, color, maxSpeed, maxLifetime));
        }
    }
    //</editor-fold>
    //<editor-fold desc="Rendering (paintComponent)">
    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        // Create a camera centered on the player
        int camX = (int)player.x - WIDTH/2;
        int camY = (int)player.y - HEIGHT/2;
        // Clamp camera to map boundaries
        camX = Math.max(0, Math.min(camX, MAP_W * TILE_SIZE - WIDTH));
        camY = Math.max(0, Math.min(camY, MAP_H * TILE_SIZE - HEIGHT));

        // Apply camera transform
        g2d.translate(-camX, -camY);

        // --- Draw world-space objects ---
        drawMap(g2d);
        drawGunPickups(g2d);
        drawParticles(g2d);
        drawBullets(g2d);
        drawEnemies(g2d);
        player.draw(g2d);
        // --- End world-space objects ---

        // Reset transform to draw screen-space UI
        g2d.translate(camX, camY); 

        // --- Draw UI objects ---
        drawUI(g2d);
        drawMiniMap(g2d);

        if (gameOver) {
            drawGameOver(g2d);
        }
    }

    private void drawMap(Graphics2D g) {
        int camX = (int)player.x - WIDTH/2;
        int camY = (int)player.y - HEIGHT/2;
        int startX = Math.max(0, camX / TILE_SIZE);
        int startY = Math.max(0, camY / TILE_SIZE);
        int endX = Math.min(MAP_W, (camX + WIDTH) / TILE_SIZE + 1);
        int endY = Math.min(MAP_H, (camY + HEIGHT) / TILE_SIZE + 1);

        for (int y = startY; y < endY; y++) {
            for (int x = startX; x < endX; x++) {
                g.setColor(TERRAIN_COLORS[map[y][x]]);
                g.fillRect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE);
            }
        }
        if (portalActive && portalPos != null) {
            g.setColor(TERRAIN_COLORS[PORTAL]);
            g.fillRect(portalPos.x * TILE_SIZE, portalPos.y * TILE_SIZE, TILE_SIZE, TILE_SIZE);
        }
    }

    private void drawGunPickups(Graphics2D g) {
        for (GunPickup gp : gunPickups) {
            gp.draw(g);
        }
    }

    private void drawEnemies(Graphics2D g) {
        for (Enemy enemy : enemies) {
            enemy.draw(g);
        }
    }

    private void drawBullets(Graphics2D g) {
        for (Bullet bullet : bullets) {
            bullet.draw(g);
        }
    }

    private void drawParticles(Graphics2D g) {
        for (Particle p : particles) {
            p.draw(g);
        }
    }

    private void drawUI(Graphics2D g) {
        g.setColor(new Color(0,0,0,150));
        g.fillRect(0,0,WIDTH, 80);
        g.fillRect(0, 80, 150, 80);

        g.setColor(Color.WHITE);
        g.setFont(new Font("Arial", Font.BOLD, 14));
        g.drawString("Level: " + level, 10, 20);
        g.drawString("Score: " + score, 10, 40);
        g.drawString("Health: " + player.health, 10, 60);

        g.drawString("Weapons:", 10, 90);
        for (int i = 0; i < 2; i++) {
            int gx = 10, gy = 100 + i * 25;
            g.setColor(i == player.selectedGun ? Color.YELLOW : Color.GRAY);
            g.drawRect(gx, gy, 120, 20);
            if (player.gunInventory[i] != -1) {
                Weapon w = weaponData.get(player.gunInventory[i]);
                g.setColor(w.color);
                g.fillRect(gx + 1, gy + 1, 118, 18);
                g.setColor(Color.BLACK);
                g.drawString(w.name, gx + 5, gy + 15);
            } else {
                g.setColor(Color.DARK_GRAY);
                g.drawString("[Empty]", gx + 5, gy + 15);
            }
        }
    }

    private void drawMiniMap(Graphics2D g) {
        int miniW = 180, miniH = 150;
        int miniX = WIDTH - miniW - 10, miniY = 10;
        g.setColor(new Color(0, 0, 0, 180));
        g.fillRect(miniX - 2, miniY - 2, miniW + 4, miniH + 4);
        double scaleX = (double)miniW / (MAP_W * TILE_SIZE);
        double scaleY = (double)miniH / (MAP_H * TILE_SIZE);

        for (Room room : rooms) {
            g.setColor(new Color(100, 100, 100, 200));
            g.fillRect(miniX + (int)(room.x1 * TILE_SIZE * scaleX), miniY + (int)(room.y1 * TILE_SIZE * scaleY),
                       (int)(room.w * TILE_SIZE * scaleX), (int)(room.h * TILE_SIZE * scaleY));
        }
        g.setColor(Color.CYAN);
        g.fillOval(miniX + (int)(player.x * scaleX) - 2, miniY + (int)(player.y * scaleY) - 2, 5, 5);
    }

    private void drawGameOver(Graphics2D g) {
        g.setColor(new Color(0, 0, 0, 200));
        g.fillRect(0, 0, WIDTH, HEIGHT);
        g.setColor(Color.RED);
        g.setFont(new Font("Arial", Font.BOLD, 50));
        String msg = "GAME OVER";
        g.drawString(msg, WIDTH/2 - g.getFontMetrics().stringWidth(msg)/2, HEIGHT/2 - 50);
        g.setColor(Color.WHITE);
        g.setFont(new Font("Arial", Font.BOLD, 20));
        msg = "Final Score: " + score;
        g.drawString(msg, WIDTH/2 - g.getFontMetrics().stringWidth(msg)/2, HEIGHT/2);
        msg = "Press 'R' to Restart";
        g.drawString(msg, WIDTH/2 - g.getFontMetrics().stringWidth(msg)/2, HEIGHT/2 + 50);
    }
    //</editor-fold>

    //<editor-fold desc="Input Handling (KeyListener)">
    @Override
    public void keyPressed(KeyEvent e) {
        int key = e.getKeyCode();
        if (gameOver && key == KeyEvent.VK_R) {
            level = 1;
            startNewGame();
            return;
        }
        player.keyPressed(e);
    }

    @Override
    public void keyReleased(KeyEvent e) {
        player.keyReleased(e);
    }

    @Override
    public void keyTyped(KeyEvent e) {}
    //</editor-fold>
    //<editor-fold desc="Data Initialization">
    private void initializeData() {
        // WEAPONS (Name, Fire Rate, Damage, Bullet Speed, Pellets, Spread, Color)
        weaponData.put(PISTOL, new Weapon("Pistol", 20, 1, 6.0, 1, 0.1, new Color(192, 192, 192)));
        weaponData.put(MAGNUM, new Weapon("Magnum", 40, 3, 8.0, 1, 0.05, new Color(100, 100, 100)));
        weaponData.put(UZI, new Weapon("Uzi", 5, 1, 7.0, 1, 0.3, new Color(150, 150, 150)));
        weaponData.put(RIFLE, new Weapon("Rifle", 15, 2, 9.0, 1, 0.08, new Color(139, 69, 19)));
        weaponData.put(SNIPER, new Weapon("Sniper", 80, 10, 15.0, 1, 0.0, new Color(0, 50, 0)));
        weaponData.put(SHOTGUN, new Weapon("Shotgun", 50, 1, 5.0, 6, 0.4, new Color(200, 100, 0)));
        weaponData.put(SAWNOFF, new Weapon("Sawn-off", 45, 1, 4.0, 10, 0.8, new Color(150, 80, 0)));
        weaponData.put(FLAMETHROWER, new Weapon("Flamethrower", 2, 1, 3.5, 3, 0.6, new Color(255, 100, 0)));
        weaponData.put(ROCKET_LAUNCHER, new Weapon("Rocket Launcher", 100, 15, 4.0, 1, 0.0, new Color(0, 100, 0)));
        weaponData.put(GRENADE_LAUNCHER, new Weapon("Grenade Launcher", 90, 12, 3.0, 1, 0.1, new Color(50, 80, 50)));
        weaponData.put(LASER_PISTOL, new Weapon("Laser Pistol", 18, 1, 10.0, 1, 0.0, new Color(255, 0, 0)));
        weaponData.put(LASER_RIFLE, new Weapon("Laser Rifle", 12, 2, 12.0, 1, 0.0, new Color(255, 50, 50)));
        weaponData.put(PLASMA_GUN, new Weapon("Plasma Gun", 25, 4, 7.0, 1, 0.1, new Color(0, 255, 255)));
        weaponData.put(RAILGUN, new Weapon("Railgun", 120, 25, 20.0, 1, 0.0, new Color(255, 255, 0)));
        weaponData.put(LIGHTNING_GUN, new Weapon("Lightning Gun", 8, 1, 8.0, 1, 0.2, new Color(255, 255, 100)));
        weaponData.put(FIRE_STAFF, new Weapon("Fire Staff", 30, 3, 6.0, 3, 0.3, new Color(255, 120, 0)));
        weaponData.put(ICE_STAFF, new Weapon("Ice Staff", 35, 2, 6.0, 5, 0.2, new Color(100, 100, 255)));
        weaponData.put(EARTH_STAFF, new Weapon("Earth Staff", 40, 5, 4.0, 1, 0.1, new Color(139, 69, 19)));
        weaponData.put(DARK_STAFF, new Weapon("Dark Staff", 25, 3, 7.0, 2, 0.15, new Color(100, 0, 100)));
        weaponData.put(HOLY_STAFF, new Weapon("Holy Staff", 28, 2, 8.0, 3, 0.05, new Color(255, 255, 200)));
        weaponData.put(THROWING_KNIVES, new Weapon("Throwing Knives", 10, 1, 8.0, 3, 0.2, new Color(200, 200, 200)));
        weaponData.put(SHURIKEN, new Weapon("Shuriken", 8, 1, 9.0, 4, 0.3, new Color(180, 180, 180)));
        weaponData.put(CROSSBOW, new Weapon("Crossbow", 35, 4, 10.0, 1, 0.0, new Color(100, 50, 0)));
        weaponData.put(REPEATER_CROSSBOW, new Weapon("Repeater X-Bow", 12, 2, 9.0, 1, 0.1, new Color(120, 70, 20)));
        weaponData.put(BOW, new Weapon("Bow", 25, 3, 8.0, 1, 0.05, new Color(180, 150, 100)));
        weaponData.put(POISON_BOW, new Weapon("Poison Bow", 30, 1, 7.0, 1, 0.05, new Color(0, 200, 50)));
        weaponData.put(MINIGUN, new Weapon("Minigun", 2, 1, 8.0, 1, 0.4, new Color(80, 80, 80)));
        weaponData.put(BUBBLE_GUN, new Weapon("Bubble Gun", 15, 1, 3.0, 1, 0.1, new Color(150, 150, 255)));
        weaponData.put(MUSIC_GUN, new Weapon("Music Gun", 18, 1, 5.0, 5, 0.5, new Color(255, 105, 180)));
        weaponData.put(VULCAN_CANNON, new Weapon("Vulcan Cannon", 1, 1, 9.0, 2, 0.3, new Color(50, 50, 50)));
        weaponData.put(ALIEN_GUN, new Weapon("Alien Gun", 22, 2, 7.0, 3, 0.25, new Color(100, 255, 100)));
        weaponData.put(GAUSS_RIFLE, new Weapon("Gauss Rifle", 50, 8, 14.0, 1, 0.0, new Color(0, 150, 255)));
        weaponData.put(NEEDLER, new Weapon("Needler", 8, 1, 8.0, 1, 0.1, new Color(255, 0, 255)));
        weaponData.put(BEAM_SWORD, new Weapon("Beam Sword", 15, 4, 10.0, 1, 0.0, new Color(0, 255, 0)));
        weaponData.put(CHAIN_GUN, new Weapon("Chain Gun", 4, 1, 8.0, 1, 0.35, new Color(110, 110, 110)));
        weaponData.put(BFG_9000, new Weapon("BFG 9000", 200, 50, 5.0, 1, 0.0, new Color(0, 255, 100)));
        weaponData.put(VOID_CANNON, new Weapon("Void Cannon", 150, 30, 6.0, 1, 0.0, new Color(50, 0, 50)));
        weaponData.put(SINGULARITY_GUN, new Weapon("Singularity Gun", 250, 100, 3.0, 1, 0.0, new Color(20, 20, 20)));
        weaponData.put(STAR_DESTROYER, new Weapon("Star Destroyer", 180, 40, 8.0, 5, 0.2, new Color(255, 215, 0)));
        weaponData.put(CHICKEN_GUN, new Weapon("Chicken Gun", 10, 1, 4.0, 1, 0.1, new Color(255, 255, 255)));
        weaponData.put(POTATO_LAUNCHER, new Weapon("Potato Launcher", 30, 2, 5.0, 1, 0.1, new Color(210, 180, 140)));
        weaponData.put(SWORD, new Weapon("Sword", 20, 3, 0.1, 1, 0.0, new Color(192, 192, 192)));
        weaponData.put(SPEAR, new Weapon("Spear", 25, 4, 0.1, 1, 0.0, new Color(200, 180, 150)));
        weaponData.put(AXE, new Weapon("Axe", 35, 6, 0.1, 1, 0.0, new Color(139, 69, 19)));
        weaponData.put(HAMMER, new Weapon("Hammer", 50, 8, 0.1, 1, 0.0, new Color(160, 160, 160)));
        weaponData.put(KATANA, new Weapon("Katana", 15, 2, 0.1, 1, 0.0, new Color(220, 220, 220)));
        weaponData.put(DUAL_PISTOLS, new Weapon("Dual Pistols", 10, 1, 6.0, 2, 0.2, new Color(192, 192, 192)));
        weaponData.put(AKIMBO_UZIS, new Weapon("Akimbo Uzis", 3, 1, 7.0, 2, 0.4, new Color(150, 150, 150)));
        weaponData.put(TRIPLE_SHOTGUN, new Weapon("Triple Shotgun", 60, 1, 5.0, 18, 0.5, new Color(220, 120, 0)));
        weaponData.put(QUAD_ROCKETS, new Weapon("Quad Rockets", 120, 15, 4.0, 4, 0.3, new Color(50, 120, 50)));

        // ENEMIES (Name, Health, Speed, Score, Behavior, Color)
        enemyData.put(GOBLIN, new EnemyData("Goblin", 3, 2.0, 10, Behavior.CHASE, new Color(0, 150, 0)));
        enemyData.put(SKELETON, new EnemyData("Skeleton", 5, 1.5, 15, Behavior.CHASE, new Color(220, 220, 220)));
        enemyData.put(SLIME, new EnemyData("Slime", 8, 1.0, 10, Behavior.CHASE, new Color(100, 200, 100)));
        enemyData.put(ORC, new EnemyData("Orc", 10, 1.8, 25, Behavior.CHASE, new Color(0, 100, 50)));
        enemyData.put(GHOST, new EnemyData("Ghost", 4, 2.5, 20, Behavior.CHASE, new Color(200, 200, 255)));
        enemyData.put(BAT, new EnemyData("Bat", 2, 3.0, 5, Behavior.CHASE, new Color(70, 70, 70)));
        enemyData.put(SPIDER, new EnemyData("Spider", 4, 2.8, 15, Behavior.CHASE, new Color(50, 50, 50)));
        enemyData.put(ZOMBIE, new EnemyData("Zombie", 12, 1.2, 20, Behavior.CHASE, new Color(100, 150, 100)));
        enemyData.put(WIZARD, new EnemyData("Wizard", 8, 1.5, 50, Behavior.SHOOT_AND_RUN, new Color(150, 0, 255)));
        enemyData.put(GOLEM, new EnemyData("Golem", 20, 0.8, 75, Behavior.CHASE, new Color(150, 150, 150)));
        enemyData.put(DEMON, new EnemyData("Demon", 15, 2.2, 100, Behavior.CHASE, new Color(200, 0, 0)));
        enemyData.put(SHADOW_ASSASSIN, new EnemyData("Shadow Assassin", 10, 3.5, 120, Behavior.CHASE, new Color(30, 30, 30)));
        enemyData.put(CYCLOPS, new EnemyData("Cyclops", 25, 1.0, 150, Behavior.CHASE, new Color(200, 150, 100)));
        enemyData.put(DRAGON_WHELP, new EnemyData("Dragon Whelp", 18, 2.5, 130, Behavior.SHOOT_AND_RUN, new Color(180, 50, 0)));
        enemyData.put(NECROMANCER, new EnemyData("Necromancer", 12, 1.4, 180, Behavior.SHOOT_AND_RUN, new Color(100, 50, 100)));
        enemyData.put(MIMIC, new EnemyData("Mimic", 10, 0.5, 200, Behavior.CHASE, new Color(139, 69, 19)));
        enemyData.put(ELEMENTAL, new EnemyData("Elemental", 15, 2.0, 110, Behavior.SHOOT_AND_RUN, new Color(0, 200, 200)));
        enemyData.put(BEHOLDER, new EnemyData("Beholder", 22, 1.2, 250, Behavior.SHOOT_AND_RUN, new Color(150, 100, 200)));
        enemyData.put(LICH, new EnemyData("Lich", 30, 1.5, 300, Behavior.SHOOT_AND_RUN, new Color(200, 255, 200)));
        enemyData.put(TITAN, new EnemyData("Titan", 50, 0.6, 500, Behavior.CHASE, new Color(255, 215, 0)));
    }
    //</editor-fold>

    //<editor-fold desc="Helper Classes, Records, and Main Method">

    // Enum for AI behavior
    enum Behavior { CHASE, SHOOT_AND_RUN }

    // Data Records for cleaner data management
    record Weapon(String name, int fireRate, int damage, double bulletSpeed, int pellets, double spread, Color color) {}
    record EnemyData(String name, int health, double speed, int scoreValue, Behavior behavior, Color color) {}

    // Base class for Player and Enemy
    abstract class Entity {
        double x, y;
        int size;
        int health, maxHealth;
        Color color;

        public Entity(double x, double y, int size, int health, Color color) {
            this.x = x;
            this.y = y;
            this.size = size;
            this.health = this.maxHealth = health;
            this.color = color;
        }

        public Rectangle getBounds() {
            return new Rectangle((int)x, (int)y, size, size);
        }

        public void draw(Graphics2D g) {
            g.setColor(color);
            g.fillOval((int)x, (int)y, size, size);

            // Draw health bar if damaged
            if (health < maxHealth) {
                g.setColor(Color.DARK_GRAY);
                g.fillRect((int)x, (int)y - 8, size, 5);
                g.setColor(Color.RED);
                g.fillRect((int)x, (int)y - 8, (int)(size * ((double)health / maxHealth)), 5);
            }
        }

        public void takeDamage(int amount) {
            this.health -= amount;
        }
    }

    class Player extends Entity {
        boolean up, down, left, right;
        boolean shootUp, shootDown, shootLeft, shootRight;
        int shootCooldown = 0;
        int[] gunInventory = {-1, -1};
        int selectedGun = 0;

        public Player(double x, double y) {
            super(x, y, PLAYER_SIZE, 10, Color.CYAN);
        }

        public void update(SoulNight game) {
            // Movement
            double speed = 3.5;
            double dx = (right ? 1 : 0) - (left ? 1 : 0);
            double dy = (down ? 1 : 0) - (up ? 1 : 0);
            double len = Math.sqrt(dx * dx + dy * dy);
            if (len != 0) {
                dx = dx / len * speed;
                dy = dy / len * speed;
            }
            if (game.isPassable(x + dx, y, size)) x += dx;
            if (game.isPassable(x, y + dy, size)) y += dy;

            // Shooting
            if (shootCooldown > 0) shootCooldown--;
            if ((shootUp || shootDown || shootLeft || shootRight) && shootCooldown == 0 && gunInventory[selectedGun] != -1) {
                int bdx = (shootRight ? 1 : 0) - (shootLeft ? 1 : 0);
                int bdy = (shootDown ? 1 : 0) - (shootUp ? 1 : 0);
                if (bdx != 0 || bdy != 0) {
                    fireWeapon(bdx, bdy, game);
                }
            }
        }

        private void fireWeapon(int bdx, int bdy, SoulNight game) {
            Weapon w = weaponData.get(gunInventory[selectedGun]);
            if (w == null) return;

            double angle = Math.atan2(bdy, bdx);
            for (int i = 0; i < w.pellets; i++) {
                double spread = (game.rand.nextDouble() - 0.5) * w.spread;
                double finalAngle = angle + spread;
                double finalSpeed = w.bulletSpeed * (1 + (game.rand.nextDouble() - 0.5) * 0.1);
                game.bullets.add(new Bullet(x + size / 2.0, y + size / 2.0,
                        Math.cos(finalAngle) * finalSpeed, Math.sin(finalAngle) * finalSpeed, false, w.damage));
            }
            shootCooldown = w.fireRate;
        }

        public void pickupGun(int gunType, SoulNight game) {
            if (gunInventory[selectedGun] == -1) {
                gunInventory[selectedGun] = gunType;
            } else if (gunInventory[(selectedGun + 1) % 2] == -1) {
                gunInventory[(selectedGun + 1) % 2] = gunType;
            } else {
                game.gunPickups.add(new GunPickup(x, y, gunInventory[selectedGun]));
                gunInventory[selectedGun] = gunType;
            }
        }

        public void keyPressed(KeyEvent e) {
            int key = e.getKeyCode();
            if (key == KeyEvent.VK_W) up = true;
            if (key == KeyEvent.VK_S) down = true;
            if (key == KeyEvent.VK_A) left = true;
            if (key == KeyEvent.VK_D) right = true;
            if (key == KeyEvent.VK_UP) shootUp = true;
            if (key == KeyEvent.VK_DOWN) shootDown = true;
            if (key == KeyEvent.VK_LEFT) shootLeft = true;
            if (key == KeyEvent.VK_RIGHT) shootRight = true;
            if (key == KeyEvent.VK_Q) selectedGun = (selectedGun + 1) % 2;
        }

        public void keyReleased(KeyEvent e) {
            int key = e.getKeyCode();
            if (key == KeyEvent.VK_W) up = false;
            if (key == KeyEvent.VK_S) down = false;
            if (key == KeyEvent.VK_A) left = false;
            if (key == KeyEvent.VK_D) right = false;
            if (key == KeyEvent.VK_UP) shootUp = false;
            if (key == KeyEvent.VK_DOWN) shootDown = false;
            if (key == KeyEvent.VK_LEFT) shootLeft = false;
            if (key == KeyEvent.VK_RIGHT) shootRight = false;
        }
    }

    class Enemy extends Entity {
        int type;
        double speed;
        Behavior behavior;
        int shootCooldown;

        public Enemy(double x, double y, int type) {
            super(x, y, ENEMY_SIZE, 1, Color.RED); // Temp values
            this.type = type;
            EnemyData data = enemyData.get(type);
            if (data != null) {
                this.health = this.maxHealth = data.health;
                this.speed = data.speed;
                this.color = data.color;
                this.behavior = data.behavior;
                this.shootCooldown = 60 + rand.nextInt(60); // Initial random cooldown
            }
        }

        public void update(SoulNight game) {
            if (shootCooldown > 0) shootCooldown--;

            Point2D.Double playerPos = new Point2D.Double(game.player.x, game.player.y);
            double distToPlayer = playerPos.distance(this.x, this.y);

            if (behavior == Behavior.SHOOT_AND_RUN) {
                if (distToPlayer < TILE_SIZE * 8) { // If player is close
                    if (shootCooldown <= 0) {
                        fireAtPlayer(game);
                    }
                    // Try to keep distance
                    move(- (playerPos.x - this.x), - (playerPos.y - this.y), game);
                } else {
                    // Wander or move towards player if too far
                    move(playerPos.x - this.x, playerPos.y - this.y, game);
                }
            } else { // CHASE behavior
                move(playerPos.x - this.x, playerPos.y - this.y, game);
            }
        }

        private void move(double dx, double dy, SoulNight game) {
            double len = Math.sqrt(dx * dx + dy * dy);
            if (len != 0) {
                dx = dx / len * speed;
                dy = dy / len * speed;
            }
            if (game.isPassable(x + dx, y, size)) x += dx;
            if (game.isPassable(x, y + dy, size)) y += dy;
        }

        private void fireAtPlayer(SoulNight game) {
            double dx = game.player.x - this.x;
            double dy = game.player.y - this.y;
            double len = Math.sqrt(dx * dx + dy * dy);
            if (len != 0) {
                dx = dx / len * 4.0; // Enemy bullet speed
                dy = dy / len * 4.0;
                game.bullets.add(new Bullet(x + size / 2.0, y + size / 2.0, dx, dy, true, 1));
                shootCooldown = 120; // Reset cooldown
            }
        }
    }

    class Bullet {
        double x, y, dx, dy;
        boolean hostile;
        int damage;
        int lifetime = 120;
        int size = BULLET_SIZE;

        public Bullet(double x, double y, double dx, double dy, boolean hostile, int damage) {
            this.x = x; this.y = y; this.dx = dx; this.dy = dy;
            this.hostile = hostile; this.damage = damage;
        }

        public void update() {
            x += dx;
            y += dy;
            lifetime--;
        }

        public void draw(Graphics2D g) {
            g.setColor(hostile ? Color.MAGENTA : Color.YELLOW);
            g.fillOval((int)x - size/2, (int)y - size/2, size, size);
        }

        public Rectangle getBounds() {
            return new Rectangle((int)x - size/2, (int)y - size/2, size, size);
        }
    }

    class Particle {
        double x, y, dx, dy;
        int lifetime;
        Color color;

        public Particle(double x, double y, Color color, double maxSpeed, int maxLifetime) {
            this.x = x;
            this.y = y;
            this.color = color;
            this.dx = (rand.nextDouble() - 0.5) * maxSpeed;
            this.dy = (rand.nextDouble() - 0.5) * maxSpeed;
            this.lifetime = rand.nextInt(maxLifetime);
        }

        public boolean update() {
            x += dx;
            y += dy;
            return --lifetime > 0;
        }

        public void draw(Graphics2D g) {
            g.setColor(color);
            g.fillRect((int)x, (int)y, 2, 2);
        }
    }

    static class Room {
        int x1, y1, x2, y2, w, h, type;
        boolean isCleared = false;
        boolean isEngaged = false;

        Room(int x, int y, int w, int h) {
            this.x1 = x; this.y1 = y; this.w = w; this.h = h;
            this.x2 = x + w; this.y2 = y + h;
        }

        int getCenterX() { return x1 + w / 2; }
        int getCenterY() { return y1 + h / 2; }

        boolean intersects(Room other) {
            return (this.x1 < other.x2 && this.x2 > other.x1 &&
                    this.y1 < other.y2 && this.y2 > other.y1);
        }

        boolean contains(int x, int y) {
            return (x >= x1 && x < x2 && y >= y1 && y < y2);
        }
    }

    class GunPickup {
        double x, y;
        int type;
        GunPickup(double x, double y, int type) {
            this.x = x; this.y = y; this.type = type;
        }
        public void draw(Graphics2D g) {
            Weapon w = weaponData.get(type);
            if (w == null) return;
            g.setColor(w.color.brighter());
            g.fillRect((int)x, (int)y, TILE_SIZE, TILE_SIZE);
            g.setColor(Color.BLACK);
            g.drawRect((int)x, (int)y, TILE_SIZE, TILE_SIZE);
        }
    }
    //</editor-fold>

    public static void main(String[] args) {
        JFrame frame = new JFrame("Soul Night - Refactored");
        SoulNight game = new SoulNight();
        frame.add(game);
        frame.pack();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);
        frame.setResizable(false);
        frame.setVisible(true);
    }
}

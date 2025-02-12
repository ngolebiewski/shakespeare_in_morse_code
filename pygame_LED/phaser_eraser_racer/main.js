class LEDRacer extends Phaser.Scene {
    constructor() {
        super({ key: 'LEDRacer' });
    }

    preload() {
        this.gridSize = 2;
        this.speed = 100;
        this.playerPos = { x: Math.floor(this.gridSize / 2), y: Math.floor(this.gridSize / 2) };
        this.playerTrail = new Set();
        this.startX = 0;
        this.startY = 0;
        this.endX = 0;
        this.endY = 0;
    }

    create() {
        this.cameras.main.setBackgroundColor('#000');
        this.calculateGridDimensions();
        
        this.input.keyboard.on('keydown', this.handleInput, this);
        this.input.on('pointerdown', this.startSwipe, this);
        this.input.on('pointerup', this.endSwipe, this);
        this.timer = this.time.addEvent({ delay: this.speed, callback: this.updateGrid, callbackScope: this, loop: true });
    }

    calculateGridDimensions() {
        this.cellSize = Math.min(window.innerWidth, window.innerHeight) / this.gridSize;
        this.offsetX = (window.innerWidth - this.gridSize * this.cellSize) / 2;
        this.offsetY = (window.innerHeight - this.gridSize * this.cellSize) / 2;
    }

    startSwipe(pointer) {
        this.startX = pointer.x;
        this.startY = pointer.y;
    }

    endSwipe(pointer) {
        this.endX = pointer.x;
        this.endY = pointer.y;
        const deltaX = this.endX - this.startX;
        const deltaY = this.endY - this.startY;
        
        if (Math.abs(deltaX) > Math.abs(deltaY)) {
            if (deltaX > 0 && this.playerPos.x < this.gridSize - 1) this.playerPos.x++;
            else if (deltaX < 0 && this.playerPos.x > 0) this.playerPos.x--;
        } else {
            if (deltaY > 0 && this.playerPos.y < this.gridSize - 1) this.playerPos.y++;
            else if (deltaY < 0 && this.playerPos.y > 0) this.playerPos.y--;
        }
    }

    updateGrid() {
        this.playerTrail.add(`${this.playerPos.x},${this.playerPos.y}`);
        if (this.playerTrail.size === this.gridSize * this.gridSize) {
            this.playerTrail.clear();
            this.gridSize++;
            // Recenter the player in the new grid
            // this.playerPos = {
            //     x: Math.floor(this.gridSize / 2),
            //     y: Math.floor(this.gridSize / 2)
            // };
            // Recalculate grid dimensions for the new size
            this.calculateGridDimensions();
        }
        this.redrawGrid();
    }

    redrawGrid() {
        this.children.removeAll();
        for (let y = 0; y < this.gridSize; y++) {
            for (let x = 0; x < this.gridSize; x++) {
                const color = this.playerTrail.has(`${x},${y}`) ? 0x000000 : Phaser.Display.Color.RandomRGB().color;
                const rect = this.add.rectangle(
                    this.offsetX + x * this.cellSize, 
                    this.offsetY + y * this.cellSize, 
                    this.cellSize, 
                    this.cellSize, 
                    color
                ).setOrigin(0);
                
                if (x === this.playerPos.x && y === this.playerPos.y) {
                    this.add.rectangle(
                        this.offsetX + x * this.cellSize + this.cellSize / 2, 
                        this.offsetY + y * this.cellSize + this.cellSize / 2, 
                        this.cellSize, 
                        this.cellSize
                    ).setStrokeStyle(3, 0xffffff);
                }
            }
        }
    }

    handleInput(event) {
        switch (event.code) {
            case 'ArrowUp':
                if (this.playerPos.y > 0) this.playerPos.y--;
                break;
            case 'ArrowDown':
                if (this.playerPos.y < this.gridSize - 1) this.playerPos.y++;
                break;
            case 'ArrowLeft':
                if (this.playerPos.x > 0) this.playerPos.x--;
                break;
            case 'ArrowRight':
                if (this.playerPos.x < this.gridSize - 1) this.playerPos.x++;
                break;
            case 'Minus':
                this.speed += 20;
                this.resetSpeed();
                break;
            case 'Equal':
                if (this.speed > 20) this.speed -= 20;
                this.resetSpeed();
                break;
        }
    }

    resetSpeed() {
        if (this.timer) {
            this.timer.remove();
        }
        this.timer = this.time.addEvent({ delay: this.speed, callback: this.updateGrid, callbackScope: this, loop: true });
    }
}

const config = {
    type: Phaser.AUTO,
    width: window.innerWidth,
    height: window.innerHeight,
    pixelArt: true,
    scene: LEDRacer
};

const game = new Phaser.Game(config);
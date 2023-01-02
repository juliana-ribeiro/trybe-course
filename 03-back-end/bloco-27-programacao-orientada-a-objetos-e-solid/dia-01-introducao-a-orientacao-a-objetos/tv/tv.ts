class Tv {
  brand: string;
  size: string;
  resolution: string;
  connections: string[];
  connectedTo?: string;

  constructor(
    brand: string,
    size: string,
    resolution: string,
    connections: string[]
  ) {
    this.brand = brand;
    this.size = size;
    this.resolution = resolution;
    this.connections = connections;
  }

  turnOn(): void {
    console.log(`TV ${this.brand} ${this.size} resolution ${this.resolution} connections ${this.connections}`)
  }
}

const tv1 = new Tv('Samsung', '32"', '1,366 x 768', ['2xHDMI', '1 USB']).turnOn();


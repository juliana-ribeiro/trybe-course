const fs = require('fs').promises;
const readline = require('readline-sync');

async function readData() {
    try {
    const fileContent = await fs.readFile('./simpsons.json', 'utf-8');
    return JSON.parse(fileContent);
    } catch (err) {
        console.error(`Failed to read file: ${err.message}`);
    }
}

async function findSimpsonById(id) {
    const simpsons = await readData();
    const getSimpson = simpsons.find((simpson) => Number(simpson.id) === id);
    if (!getSimpson) {
        throw new Error('Id not found');
    }
    return getSimpson;
}

async function main() {
    const id = readline.questionInt("Choose Simpson's id: ");
    console.log(await findSimpsonById(id));
}

main();
const readline = require('readline-sync');

const weight = readline.questionFloat(`What's your weight in kg?`);
const height = readline.questionFloat(`What's your height in cm?`);

const bmiFormula = () => +(weight / (height ** 2)).toFixed(2);

const handleBMI = () => {
    const calc = bmiFormula();
    if(calc < 18.5) return `BMI: ${calc} | Category: Underweight`;
    if(calc <= 24.9) return `BMI: ${calc} | Category: Normal weight`;
    if(calc <= 29.9) return `BMI: ${calc} | Category: Overweight`;
    if(calc <= 34.9) return `BMI: ${calc} | Category: Obesity I`;
    if(calc <= 39.9) return `BMI: ${calc} | Category: Obesity II`;
    if(calc >= 40) return `BMI: ${calc} | Category: Obesity III and IV`;
}

console.log(handleBMI());
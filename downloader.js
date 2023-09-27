const instateLetters = () => document.querySelector(".friend-letters-wrapper").children[0].children;
const clickLetter = (reference) => reference.click();
const goBack = () => document.querySelector(".icon-caret-right").click();
const getLetterText = () => document.querySelector(".pre-wrap").textContent;
const getLetterAuthor = () => document.querySelector(".mb-1").textContent;
const getLetterDate = () => document.querySelector("span.text-light.small.pr-1.ml-n1").textContent;
const printData = (...args) => {
    for (let _ = 0; _ < args.length; _++)
    {
        console.log(args[_])
    }
};

let outputString = "";

let letters = instateLetters();
let author, date, text;
for (let i = 0; i < letters.length; i++)
{
    letters = instateLetters();
    clickLetter(letters[i].children[0]);
    text = getLetterText();
    author = getLetterAuthor();
    date = getLetterDate();
    printData(text, author, date);
    outputString+=`${JSON.stringify(text.replace(/"/g,"'"))},${author},${date}\n`;
    goBack();
};
console.log(outputString)
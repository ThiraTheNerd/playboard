console.log('Hello World')

const copyBtns = [...document.getElementsByClassName('copy-btn')]
console.log(copyBtns)

function selfCopy(copyText)
{
  navigator.clipboard.writeText(copyText);
  alert('THIS BUTTON HAS BEEN CLICKED')
}
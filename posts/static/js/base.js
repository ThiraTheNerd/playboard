console.log('Hello World')

copyLink = (element) => {
  document.getElementById(element).select();
  document.execCommand("copy")
}

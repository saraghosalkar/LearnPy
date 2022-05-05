function check()
{
count=0
option=document.querySelectorAll('input[type=radio]')
console.log(option.length)
for(i=0;i<option.length;i++)
{
   if(option[i].checked)
   {
       count++
   }
   if(count==5)
   {
       break
   }
}
// console.log(count)
// alert("Hey")
if(count<5)
{
    console.log(count)
    alert("Please attempt all the questions")
   
}
}
//SnackBar
function Snackbar() {
    var x = document.getElementById("snackbar");
    x.className = "show";
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
  }
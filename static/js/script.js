$(document).ready(function(){
    $('.sidenav').sidenav();
  });
        
 // select initialization
 let selects = document.querySelectorAll("select");
 M.FormSelect.init(selects);

 // collapsible initializataion
 let collapsibles = document.querySelectorAll(".collapsible");
 M.Collapsible.init(collapsibles);

 //collapsable for the starter, drinks, main, desserts
 $(document).ready(function(){
  $('.collapsible').collapsible();
});
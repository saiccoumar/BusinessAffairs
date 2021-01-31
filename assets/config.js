function opener(panel, link) {
    var i, tabcontent, tablink;
    
    tabcontent = document.getElementsByClassName('tabcontent');
    tablink = document.getElementsByClassName('tablink');
    
    for(i=0; i<tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
        tablink[i].classList.remove('active');
    }
    
    document.getElementById(panel).style.display = "block";
    link.classList.add('active');
}

document.getElementById('default').click();
function opener(panel, link) {
    var i, tabcontent, tablink;
    
    // Get all tab contents
    tabcontent = document.getElementsByClassName('tabcontent');
    tablink = document.getElementsByClassName('tablink');
    
    // Remove the active display tags and hide
    for (i=0; i<tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
        tablink[i].classList.remove('active');
    }
    
    // Show the correct pane
    document.getElementById(panel).style.display = "block";
    link.classList.add('active');
}

function saveExit() {
    var videoDev, audioDev, behaviors, people, keybinds;

    // Pull from input values
    videoDev = document.getElementById('videoInput').value;
    audioDev = document.getElementById('audioInput').value;

    behaviors = [false, false, false, false];
    for (i=1; i<5; i++) {
        behaviors[i] = document.getElementById(`beh${i}`).checked;
    }

    people = document.getElementById('numPeople').value;

    keybinds = [null, null, null];
    for (i=1; i<4; i++) {
        keybinds[i] = document.getElementById(`key${i}`).value;
        console.log(keybinds[i])
    }

    // Send to Python which will take care of the rest
    pywebview.api.configSaveExit(videoDev, audioDev, behaviors, people, keybinds);
}

document.getElementById('default').click();
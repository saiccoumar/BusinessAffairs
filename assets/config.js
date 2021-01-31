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

    // Write current and then read preferences
    displayPrefs();
    writePrefs();
}

function displayPrefs() {
    pywebview.api.readSettings().then(function(response) {
        prefs = response;

        // Place values
        document.getElementById('videoInput').value = prefs[0][1];
        document.getElementById('audioInput').value = prefs[0][0];

        for (i=0; i<4; i++) {
            mark = false;
            if (prefs[1][i]) {
                mark = true;
            } else {
                mark = false;
            }
            document.getElementById(`beh${i}`).checked = mark;
        }

        document.getElementById('numPeople').value = prefs[1][4]

        for (i=0; i<4; i++) {
            document.getElementById(`key${i}`).value = prefs[2][i];
        }
    })
}

function writePrefs() {
    var videoDev, audioDev, behaviors, people, keybinds;

    // Pull from input values
    videoDev = document.getElementById('videoInput').value;
    audioDev = document.getElementById('audioInput').value;

    behaviors = [false, false, false, false];
    for (i=0; i<4; i++) {
        behaviors[i] = document.getElementById(`beh${i}`).checked;
    }

    people = document.getElementById('numPeople').value;

    keybinds = [null, null, null, null];
    for (i=0; i<4; i++) {
        keybinds[i] = document.getElementById(`key${i}`).value;
    }

    // Send to Python which will take care of the rest
    pywebview.api.writeSettings(videoDev, audioDev, behaviors, people, keybinds);
}

function saveExit() {
    writePrefs();
    pywebview.api.configSaveExit();
}

document.getElementById('default').click();
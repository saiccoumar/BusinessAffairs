var power = false;
var configOpen = false;
var started = false;

function updateRunning() {
    // Remove existing status colors
    document.getElementById('power').classList.remove('monitorOn');
    document.getElementById('power').classList.remove('monitorOff');

    // Update running status in Python
    pywebview.api.updateRunning(!power);

    // Start detecting process in Python if not started
    if (!started) {
        pywebview.api.detecting();
        started = true;
    }
    

    if (!power) {
        // Turn monitoring on
        power = true;

        // Change colors
        document.getElementById('powerText').innerText = "MONITORING";
        document.getElementById('power').classList.add('monitorOn');
        document.getElementById('logo').src="logo.svg";
    } else {
        // Turn off monitoring
        power = false;

        // Change colors
        document.getElementById('powerText').innerText = "Sleeping";
        document.getElementById('power').classList.add('monitorOff');
        document.getElementById('logo').src="logo_sleep.svg";
    }
}

function openConfig() {
    pywebview.api.createConfigWindow();
}
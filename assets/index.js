var power = false;

document.getElementById('power').click();

function updateRunning() {
    // Remove existing status colors
    document.getElementById('power').classList.remove('monitorOn');
    document.getElementById('power').classList.remove('monitorOff');

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

    pywebview.api.detecting();
    pywebview.api.updateRunning(power);

    // var status = document.getElementById('power').value;
    // if(status == "Monitoring"){
    //     document.getElementById('power').value = "Not Monitoring";
    // } else {
    //     document.getElementById('power').value = "Monitoring";
    // }
    // pywebview.api.updateRunning(status);
    // if(!started){
    //     pywebview.api.detecting();
    //     started = true;
    // }
}

function detecting() {
    pywebview.api.detecting();
}
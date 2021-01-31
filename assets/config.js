displayed = false;

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

    if (!displayed) {
        displayPrefs();
        displayed = true;
    }
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



function lengthString(){
    textarea=document.getElementById("key0");
    var order = textarea.value;
    if(order.length==12||order.length==6){
        document.getElementById("key0").disabled = true;
        //console.log("Hello Jason Leong");
    }
    else if(order.length==7&&(order!="Ctrl")){
        document.getElementById("key0").disabled = true;
    }
   
}

   



count = 0;
textarea = document.getElementById("key0");




words=["","",""];
count=0;
textarea = document.getElementById("key0");

function unbind(){
textarea.value="";
for(i=0;i<3;i++){
words[i]="";
}
count=0;
}

function updateText(){
textarea.value="";
if(count==1)
textarea.value=words[0];
else if(count==2)
textarea.value=words[0]+"+"+words[1];
else if(count==3)
textarea.value=words[0]+"+"+words[1]+"+"+words[2];
}

function keyPress(e) {
var evtobj = window.event? event : e
if(!words.includes(evtobj.key)){
if(evtobj.key=="Control"){
words[count]="Ctrl";
}
else{
words[count]=evtobj.key;
}
count++;
sort();
}
if(count>3){
unbind();
}
console.log(words[0]+" "+words[1]+" "+words[2]);
updateText();
lengthString()
}

function sort(){
if(count==2 && words[1]=="Ctrl")
swap(0,1);
if(count==2 && words[1]=="Shift" && !words.includes("Ctrl"))
swap(0,1);
if(count==3 && words[2]=="Ctrl")
swap(0,2);
if(count==3 && words[2]=="Shift" && !words.includes("Ctrl"))
swap(0,2);
if(count==3 && words[2]=="Shift" && words.includes("Ctrl"))
swap(1,2);
}

function swap(i1,i2){
s1=words[i1];
words[i1]=words[i2];
words[i2]=s1;
}

textarea.onkeyup=keyPress;
textarea.onclick=unbind;





// document.onkeydown = KeyPress;

function truePress(){
    textarea=document.getElementById("key0");
    textarea.value="";
    //document.getElementById("key0").disabled = false;
}
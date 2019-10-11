// mit freundlicher Unterstützung von Vincenz :-) (Dankeschön)

function fields(active) {
    if (active == 1){
    document.getElementById("minute").disabled = false;
    document.getElementById("tagStunde").disabled = true;
    document.getElementById("tagMinute").disabled = true;
    document.getElementById("monatTag").disabled = true;
    document.getElementById("monatStunde").disabled = true;
    document.getElementById("monatMinute").disabled = true;
}
else if (active == 2){
    document.getElementById("tagStunde").disabled = false;
    document.getElementById("tagMinute").disabled = false;
    document.getElementById("minute").disabled = true;
    document.getElementById("monatTag").disabled = true;
    document.getElementById("monatStunde").disabled = true;
    document.getElementById("monatMinute").disabled = true;
}
else if (active == 3){
    document.getElementById("monatTag").disabled = false;
    document.getElementById("monatStunde").disabled = false;
    document.getElementById("monatMinute").disabled = false;
    document.getElementById("minute").disabled = true;
    document.getElementById("tagStunde").disabled = true;
    document.getElementById("tagMinute").disabled = true;
}
}
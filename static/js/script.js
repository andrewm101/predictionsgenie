/* draggable elements */
const item = document.querySelectorAll('.item');

/* drop targets */
const boxes = document.querySelectorAll('.droppable');

item.forEach(elem=> {
    elem.addEventListener('dragstart', dragStart);
});

function dragStart(event) {
    event.dataTransfer.setData('text/plain', event.target.id);
    setTimeout(() => {
        event.target.classList.add('hide');
    }, 0);
}

boxes.forEach(box => {
    box.addEventListener('dragenter', dragEnter)
    box.addEventListener('dragover', dragOver);
    box.addEventListener('dragleave', dragLeave);
    box.addEventListener('drop', drop);
});

/*  checks if the home/away drop in containers already
    contain an element. If no element is present, enables
    currently dragged eleemnt to be entered in the box */
function dragEnter(event) {
    if(!event.target.classList.contains("dropped")) {
        event.target.classList.add("droppable-hover");
    }
}

/*  checks if the home/away drop in containers already
    contain an element, if no element is present, box border
    changes to indicated that the box drag zone has been entered */
function dragOver(event) {
    if(!event.target.classList.contains("dropped")) {
        event.preventDefault(); // Prevent default to allow drop
    }
}

function dragLeave(event) {
    if(!event.target.classList.contains("dropped")) {
        event.target.classList.remove("droppable-hover");
    }
    event.target.classList.remove('drag-over');
}

const team_data_map = new Map();
function drop(event) {

    // This is in order to prevent the browser default handling of the data
    event.preventDefault();
    event.target.classList.remove('drag-over');
    // gets the id of the dragged element (i.e: Manchester, Leeds, etc...)
    const id = event.dataTransfer.getData('text/plain');

    const draggable = document.getElementById(id);
    // add it to the drop target
    event.target.appendChild(draggable);
    draggable.classList.remove('hide');
    event.target.classList.remove("droppable-hover");

    /*get team name and whether they are home/away and put into mapping */
    const draggableElementData = event.dataTransfer.getData("text");
    const droppableElementData = event.target.getAttribute("data-draggable-id");
    team_data_map.set(droppableElementData, id);

    const draggableElement = document.getElementById(draggableElementData);
    event.target.classList.add("dropped");
    draggableElement.classList.add("dragged");
    draggableElement.setAttribute("draggable", "false");
  }

  function send_data(){
    // Need to output message for error
    // telling user both boxes must be filled
    if(team_data_map.size > 1){
        fetch(`/getPredictions/${team_data_map.get('home')}/${team_data_map.get('away')}`)
            .then(function (response) {
                return response.json()
            }).then(function (text) {
                let jsonData_string = (JSON.stringify(text));
                console.log(jsonData_string);
                let probabilities = new Array();
                while(jsonData_string.indexOf('.') != -1){
                    let start_idx = jsonData_string.indexOf('.') - 1;
                    let end_idx = jsonData_string.indexOf('.') + 3;
                    probabilities.push(jsonData_string.substring(start_idx, end_idx));
                    jsonData_string = jsonData_string.substr(end_idx);
                }
                console.log(probabilities);
                for(let home = 0; home <=4; home++){
                    for(let away = 0; away <=4; away++){
                        let score_id = "(" + home + ", " + away + ")";
                        document.getElementById(String(score_id)).innerHTML = String(probabilities[home + away])+ "%";
                    }
                }
            });
        showDiv();
    }
  }

  function showDiv() {
    document.getElementById('sign-in').style.display = "block";
  }
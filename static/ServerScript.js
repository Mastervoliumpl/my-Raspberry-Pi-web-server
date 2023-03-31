function toggle(button) {
    var id = button.getAttribute("data-id");
    var state = button.getAttribute("data-state");
    if (state === "off") {
      button.classList.add("on");
      button.setAttribute("data-state", "on");
      button.textContent = "LED " + id + " ON";
      var url = "/led/" + id + "/on";
      var xhr = new XMLHttpRequest();
      xhr.open("GET", url);
      xhr.send();
    } else {
      button.classList.remove("on");
      button.setAttribute("data-state", "off");
      button.textContent = "LED " + id + " OFF";
      var url = "/led/" + id + "/off";
      var xhr = new XMLHttpRequest();
      xhr.open("GET", url);
      xhr.send();
    }
  }

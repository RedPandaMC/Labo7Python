document.addEventListener("DOMContentLoaded", () => {
  const currentPage = document.querySelector("title").textContent;
  var request = new XMLHttpRequest();
  request.open("GET", "data.json", true);
  request.onreadystatechange = function () {
    if (request.readyState === 4 && request.status === 200) {
      var my_JSON_object = JSON.parse(request.responseText);
      var links = [];
      my_JSON_object.forEach((link) => {
        if (!(link.includes(currentPage))) {
          links.push(link);
        }
      });
      links.sort((a, b) => {
        if (a.indexOf("home") != -1) {
          return -1;
        } else if (b.indexOf("home") != -1) {
          return 1;
        } else {
          return a.localeCompare(b);
        }
      });
      var ul = document.getElementById("page-links");
      links.forEach((link) => {
        var li = document.createElement("li");
        var a = document.createElement("a");
        a.href = link;
        if (link.includes("__")) {
          a.textContent = link.slice(0, link.indexOf("__"));
        } else {
          a.textContent = link.slice(0, link.indexOf(".html"));
        }
        li.append(a);
        ul.appendChild(li);
      });
    }
  };
  request.send(null);
});

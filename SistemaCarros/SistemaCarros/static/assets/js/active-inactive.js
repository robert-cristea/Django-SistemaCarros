var active = document.getElementById('active')
  for (var i = 0; i < active.children.length; i++) {
    var li = actives.children[i]
    if (li === e.target) {
      /*
       If the <li> inside the current loop matches our clicked element (e.target),
       append active class to it
      */
      li.classList.add('active')
    } else {
      /*. */
      li.classList.remove('active')
    }
  }
})
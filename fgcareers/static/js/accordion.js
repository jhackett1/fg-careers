export default () => {
    const buttons = document.querySelectorAll(".benefits__button")
    const benefits = document.querySelectorAll(".benefits__benefit")
    const allContent = document.querySelectorAll(".benefits__benefit-content")

    buttons.forEach(button => {
        button.addEventListener("click", e => {
            // unselect all
            allContent.forEach(content => content.setAttribute("hidden", "true"))
            benefits.forEach(benefit => benefit.classList.remove("benefits__benefit--open"))
            buttons.forEach(benefit => benefit.classList.remove("benefits__button--open"))
            // get parent node
            let parent = e.target.parentNode
            if(parent.classList[0] == "benefits__button") parent = parent.parentNode
            // make chosen node visible
            button.classList.add("benefits__button--open")
            parent.classList.add("benefits__benefit--open")
            parent.querySelector(".benefits__benefit-content").removeAttribute("hidden")
        })
    })
}
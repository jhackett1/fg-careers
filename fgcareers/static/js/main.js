import "slick-carousel/slick/slick.css"
import "slick-carousel/slick/slick-theme.css"
import "../scss/_style.scss"

import $ from "jquery"
import "slick-carousel"
import initAccordion from "./accordion"

document.addEventListener("DOMContentLoaded", () => {
    initAccordion()



    $(".testimonials__list").slick({
        arrows: false,
        dots: true
    })


})
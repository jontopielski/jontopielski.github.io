const galleryImages = document.querySelectorAll(".artPanel");
const modal = document.querySelector(".modal");

galleryImages.forEach((image) => {
    image.addEventListener("click", () => {
        modal.style.display = "block";

        const enlargedImage = document.createElement("img");
        enlargedImage.src = image.src;
        enlargedImage.classList.add("enlargedImage");
        modal.appendChild(enlargedImage);
    });
});

modal.addEventListener("click", (event) => {
    if (event.target === modal) {
        modal.style.display = "none";
        modal.innerHTML = "";
    }
});

document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
        modal.style.display = "none";
        modal.innerHTML = "";
    }
});
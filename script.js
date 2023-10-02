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

const links = document.querySelectorAll('a');

links.forEach(link => {
  const range = document.createRange();
  range.selectNodeContents(link);

  const textNodes = Array.from(range.extractContents().childNodes);
  textNodes.forEach(textNode => {
    if (textNode.nodeType === Node.TEXT_NODE) {
      textNode.textContent = textNode.textContent.trim();
    }
  });

  textNodes.forEach(textNode => {
    link.appendChild(textNode);
  });
});

function adjustFontSize() {
  const textElements = document.querySelectorAll(".navs");
  const fontSize = window.innerWidth < 400 ? '20px' : '24px';
  textElements.forEach(function (textElement) {
    textElement.style.fontSize = fontSize;
  });
}

window.addEventListener('load', adjustFontSize);
window.addEventListener('resize', adjustFontSize);

function adjustGrid() {
  const gridElement = document.querySelector('.grid');
  const viewportWidth = window.innerWidth;

  if (viewportWidth <= 1000) {
    gridElement.style.gridTemplateColumns = 'repeat(auto-fill, minmax(160px, 1fr))';
  } else {
    gridElement.style.gridTemplateColumns = 'repeat(5, 1fr)';
  }
}

window.addEventListener('load', adjustGrid);
window.addEventListener('resize', adjustGrid);
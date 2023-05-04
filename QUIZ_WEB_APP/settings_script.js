function changeColorCategory(category) {
    // удаляем класс "active" у всех категорий
    const categories = document.querySelectorAll('.category');
    categories.forEach((item) => {
      item.classList.remove('active');
    });
    
    // добавляем класс "active" к выбранной категории
    category.classList.add('active');
  }

  function changeColorMode(category) {
    // удаляем класс "active" у всех категорий
    const categories = document.querySelectorAll('.mode');
    categories.forEach((item) => {
      item.classList.remove('active');
    });
    
    // добавляем класс "active" к выбранной категории
    category.classList.add('active');
  }


  const questionsInput = document.querySelector("#questions")
  const questionsValue = document.getElementById("questions-value");
  
  questionsInput.addEventListener("input", () => {
    questionsValue.textContent = `${questionsInput.value} вопросов`;
  });
  
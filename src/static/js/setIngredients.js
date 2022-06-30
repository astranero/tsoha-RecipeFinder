var ingredient_input = document.getElementById('ingredient_input');
      var add_more_fields = document.getElementById('add_more_fields');
      var remove_fields = document.getElementById('remove_fields');

      add_more_fields.onclick = function(){

      var newRow = document.createElement('div');
      ingredient_input.appendChild(newRow);

      var newIngredient = document.createElement('input');
      newIngredient.setAttribute('type','text');
      newIngredient.setAttribute('class','survey_ingredient');
      newIngredient.setAttribute('name','ingredient');
      newIngredient.setAttribute('id','ingredient');
      newIngredient.setAttribute('placeholder','Add ingredient');
      ingredient_input.appendChild(newIngredient);
      }

      remove_fields.onclick = function(){
          const element = document.getElementById("ingredient_input");
          element.removeChild(element.lastChild);
      }
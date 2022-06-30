var ingredient_input = document.getElementById('ingredient_input');
        var add_more_fields = document.getElementById('add_more_fields');
        var remove_fields = document.getElementById('remove_fields');
        add_more_fields.onclick = function(){

        var newRow = document.createElement('div');
        ingredient_input.appendChild(newRow);

        var newIngredient = document.createElement('input');
        newIngredient.setAttribute('type','text');
        newIngredient.setAttribute('class', 'form-control')
        newIngredient.setAttribute('name','new_ingredient');
        newIngredient.setAttribute('id','new_ingredient');
        newIngredient.setAttribute('placeholder','Write ingredient name here');
        ingredient_input.appendChild(newIngredient);
        }

        remove_fields.onclick = function(){
            const element = document.getElementById("ingredient_input");
            element.removeChild(element.lastChild);
        }
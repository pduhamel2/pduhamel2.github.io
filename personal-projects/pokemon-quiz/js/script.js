const pokemonList = [
  { id: 0, name: " ", image: " " }, { id: 0, name: " ", image: " " }, { id: 0, name: " ", image: " " },
  { id: 0, name: " ", image: " " }, { id: 0, name: " ", image: " " }, { id: 0, name: " ", image: " " },
  { id: 0, name: " ", image: " " }, { id: 0, name: " ", image: " " }, { id: 0, name: " ", image: " " },
  { id: 0, name: " ", image: " " }, { id: 0, name: " ", image: " " }, { id: 0, name: " ", image: " " },
  { id: 0, name: " ", image: " " }, { id: 0, name: " ", image: " " }, { id: 0, name: " ", image: " " },
  { id: 0, name: " ", image: " " }, { id: 0, name: " ", image: " " }, { id: 0, name: " ", image: " " },
  { id: 0, name: " ", image: " " }, { id: 0, name: " ", image: " " }
]

const trainers = [
  { name: "Jr.", image: "https://cdn.bulbagarden.net/upload/2/23/Spr_FRLG_Camper.png" }, { name: "PokéManiac", image: "https://cdn.bulbagarden.net/upload/0/0e/Spr_FRLG_Pok%C3%A9Maniac.png" },
  { name: "Super Nerd", image: "https://cdn.bulbagarden.net/upload/1/1f/Spr_FRLG_Super_Nerd.png" }, { name: "Gym Leader", image: "https://cdn.bulbagarden.net/upload/d/dd/Spr_FRLG_Sabrina.png" },
  { name: "Elite Four", image: "https://cdn.bulbagarden.net/upload/f/fb/Spr_FRLG_Lance.png" }
]

var currentPokemon = 0;
var currentScore = 0;

function populatePokemonList() {
  pokemonList.forEach(function (pokemon) {
    let id = Math.floor(Math.random() * 151) + 1;
    catchPokemon(pokemon, id);
  });
}

function catchPokemon(pokemon, id) {
  let pokeURL = "https://pokeapi.co/api/v2/pokemon/" + id;

  $.ajax({
    type: "GET",
    url: pokeURL,
    contentType: "text/plain",
    headers: {},
    success: function (data) {
      let duplicate = false;
      for (let i = 0; i < pokemonList.length; i++) {
        if (parseInt(data.id) === parseInt(pokemonList[i].id)) {
          duplicate = true;
          let newID = Math.floor(Math.random() * 151) + 1;
          catchPokemon(pokemon, newID);
          break;
        }
      }
      if (!duplicate) {
        pokemon.id = data.id;
        pokemon.name = data.name[0].toUpperCase() + data.name.slice(1);
        pokemon.image = data.sprites.front_default;
        updateProgressBar();
      }
    },
    error: function () {
      catchPokemon(pokemon, id);
    }
  });
}

function updateProgressBar() {
  var loadingProgress = parseInt($(".progress-bar").attr("aria-valuenow")) + 5;
  $(".progress-bar").css("width", loadingProgress + "%").attr("aria-valuenow", loadingProgress);
  if (loadingProgress === 100) {
    setTimeout(function () {
      $("h2").html("Ready!");
      $("#start-button").fadeIn()
    }, 600);
  }
}

function manageQuiz() {
  let randomPokemon1 = Math.floor(Math.random() * pokemonList.length);
  if (randomPokemon1 === currentPokemon && randomPokemon1 < pokemonList.length) {
    randomPokemon1++;
  } else if (randomPokemon1 === currentPokemon && randomPokemon1 === pokemonList.length) {
    randomPokemon1--;
  }
  let randomPokemon2 = Math.floor(Math.random() * pokemonList.length);
  if ((randomPokemon2 === currentPokemon || randomPokemon2 === randomPokemon1) && randomPokemon2 < pokemonList.length) {
    randomPokemon2++;
    if ((randomPokemon2 === currentPokemon || randomPokemon2 === randomPokemon1) && randomPokemon2 < pokemonList.length) {
      randomPokemon2++;
    } else if ((randomPokemon2 === currentPokemon || randomPokemon2 === randomPokemon1) && randomPokemon2 === pokemonList.length) {
      randomPokemon2 -= 3;
    }
  } else if ((randomPokemon2 === currentPokemon || randomPokemon2 === randomPokemon1) && randomPokemon2 === pokemonList.length) {
    randomPokemon2--;
    if ((randomPokemon2 === currentPokemon || randomPokemon2 === randomPokemon1) && randomPokemon2 < pokemonList.length) {
      randomPokemon2--;
     }
  }
  let correctAnswer = Math.floor(Math.random() * 3) + 1;
  $("#main-image").attr("src", pokemonList[currentPokemon].image);
  switch (correctAnswer) {
    case 1:
      $("#answer-1").html(pokemonList[currentPokemon].name);
      $("#answer-2").html(pokemonList[randomPokemon1].name);
      $("#answer-3").html(pokemonList[randomPokemon2].name);
      break;
    case 2:
      $("#answer-1").html(pokemonList[randomPokemon1].name);
      $("#answer-2").html(pokemonList[currentPokemon].name);
      $("#answer-3").html(pokemonList[randomPokemon2].name);
      break;
    case 3:
      $("#answer-1").html(pokemonList[randomPokemon1].name);
      $("#answer-2").html(pokemonList[randomPokemon2].name);
      $("#answer-3").html(pokemonList[currentPokemon].name);
      break;
    default:
      $("#answer-1").html(pokemonList[currentPokemon].name);
      $("#answer-2").html(pokemonList[randomPokemon1].name);
      $("#answer-3").html(pokemonList[randomPokemon2].name);
      break;
  }
}

function nextQuestion() {
  $("h2").html("Who's that Pokémon?");
  $(".answer").removeClass("correct");
  $(".answer").removeClass("wrong");
  $(".answer").removeClass("disable-button");
}

function results() {
  $("#main-image").addClass("trainer-image");
  $(".answer").remove();
  $("#final-score").removeClass("hidden");
  $("#final-score").html("You got " + currentScore + " out of 20 Correct!")
  if (currentScore <= 4) {
    $("h2").html("You're A " + trainers[0].name + " Trainer!");
    $("#main-image").attr("src", trainers[0].image);
  } else if (currentScore <= 9) {
    $("h2").html("You're A " + trainers[1].name + "!");
    $("#main-image").attr("src", trainers[1].image);
  } else if (currentScore <= 14) {
    $("h2").html("You're A " + trainers[2].name + "!");
    $("#main-image").attr("src", trainers[2].image);
  } else if (currentScore <= 19) {
    $("h2").html("You're A " + trainers[3].name + "!");
    $("#main-image").attr("src", trainers[3].image);
  } else if (currentScore === 20) {
    $("h2").html("You're An " + trainers[4].name + " Trainer!");
    $("#main-image").attr("src", trainers[4].image);
  }
}

$("#start-button").click(function () {
  $("h2").html("Who's that Pokémon?");
  $("#start-button").remove();
  $("#progress-bar-container").remove();
  manageQuiz();
  $("#quiz-container").fadeIn()
});

$(".answer").click(function () {
  let answer = $(this).text();
  if (answer === pokemonList[currentPokemon].name) {
    $("h2").html("It's " + pokemonList[currentPokemon].name + "!");
    $(this).addClass("correct");
    currentScore++;
  } else {
    $("h2").html("Nice try, it's " + pokemonList[currentPokemon].name + "!");
    $(this).addClass("wrong");
  }
  $(".btn").blur();
  $(".btn").focusout();
  $("#main-image").focus();
  $(".answer").addClass("disable-button");
  currentPokemon++;
  setTimeout(function () {
    if (currentPokemon < pokemonList.length) {
      manageQuiz();
      nextQuestion();
    } else {
      results();
    }
  }, 2500);
})

$("#new-game").click(function () {
  let reload = confirm("Are you sure you want to start a new game?");
  if (reload === true) {
    location.reload();
  }
})

$(document).ready(populatePokemonList());

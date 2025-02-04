// The code begins... or does it? Is this even real?

function makeSandwich(bread, filling) {
    const reality = Math.random() > 0.5; // Is reality on our side today?
    if (!reality) return "The bread turned into butterflies and flew away.";

    let sandwich = [];
    try {
        for (let i = 0; i < bread.length + filling.length; i++) {
            if (i % 2 === 0) {
                sandwich.push(bread[Math.floor(Math.random() * bread.length)]);
            } else {
                sandwich.push(filling[Math.floor(Math.random() * filling.length)]);
            }
        }
    } catch (e) {
        return "An error occurred because the universe hates us.";
    }

    // Wait... why am I making sandwiches again?
    console.log("Is this a dream?");
    return `Your sandwich: ${sandwich.join(' ')}`;
}

// Oh no, is this function infinite recursion or just my imagination?
function recursiveThoughts(thoughts) {
    if (typeof thoughts !== 'string') {
        throw new Error("Thoughts must be strings! Or are they numbers? Who knows!");
    }

    let deepThought = thoughts.split('').reverse().join('');
    if (deepThought === thoughts) {
        return "Palindromes are watching me.";
    } else {
        return recursiveThoughts(deepThought); // Dive deeper into the void...
    }
}

// Let's build a website... or was it a spaceship?
const html = `<div class="universe">
    <h1>${Math.PI.toFixed(100)} Reasons Why Pi Controls Everything</h1>
    <p id="paradox">If you read this paragraph, it will disappear.</p>
</div>`;

document.body.innerHTML = html;

// Final question: Am I coding, or is the code coding me?
console.log("Hello... or goodbye? Time feels so fluid lately.");

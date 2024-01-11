gsap.registerPlugin(ScrollToPlugin)

const nav = $('nav');
var currGenerator; //Needed for form.js

function fillContent(generator_name){

    currGenerator = generator_name;
    
    $("#SecOutput").hide();    
    $("#SecTests").hide();
    $("form button").removeClass("clickedOnce")

    gsap.to(window, { duration: 1, scrollTo: $("#SecInfo").position().top ,ease: "power2" });

    nav.find('ul>li').removeClass('selected')

    const secInfo = $('#SecInfo')
    const form = $("#myform");

    const lorem_ipsum_txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eleifend ornare ultrices. Vestibulum mauris mauris, interdum vel vulputate in, dictum quis risus. Suspendisse vehicula facilisis dolor id porta. Nullam convallis augue tristique egestas consequat. Proin a pretium nunc. Ut aliquam velit at sodales viverra. Donec dignissim molestie nunc sed sollicitudin. Curabitur pretium quis purus suscipit ultricies. Phasellus lacinia est lorem, et hendrerit metus sollicitudin sit amet. Aliquam tempus bibendum aliquet."

    switch(generator_name){

        case "Xoshiro":
            nav.find('ul>li').eq(0).addClass('selected');

            var infoContent = `
                <h1>Generator Xoshiro256</h1>
                <p>Opis alg. generatora, jego parametry, origin story itd.</p>
                <p>${lorem_ipsum_txt}</p>`;
            secInfo.html(infoContent)

            var formContent = `
                <div>
                    <label>seed</label>
                    <input type="text" name="seed" size="10" placeholder="30"/>
                </div>
                <div>
                    <label>bit size</label>
                    <input type="text" name="bitsize" size="10" placeholder="50 "/>
                </div>
            `;
            form.find("#formContent").html(formContent)

            break;
        
        case "MSWS":
            nav.find('ul>li').eq(1).addClass('selected');

            var infoContent = `
                <h1>Generator Middle SquareWeyl Sequence</h1>
                <p>Opis alg. generatora, jego parametry, origin story itd.</p>
                <p>${lorem_ipsum_txt}</p>`;
            secInfo.html(infoContent)

            var formContent = `
                <div>
                    <label>seed</label>
                    <input type="text" name="seed" size="10" placeholder="1234"/>
                </div>
                <div>
                    <label>bit size</label>
                    <input type="text" name="bitsize" size="10" placeholder="30"/>
                </div>
            `;
            form.find("#formContent").html(formContent)

            break;

        case "MM":
            nav.find('ul>li').eq(2).addClass('selected');
            
            var infoContent = `
                <h1>Generator McLaren-Marsaglia</h1>
                <p>Opis alg. generatora, jego parametry, origin story itd.</p>
                <p>${lorem_ipsum_txt}</p>`;
            secInfo.html(infoContent)

            var formContent = `
            
                <div>
                    <label>X</label>
                    <input type="text" name="X" size="30" placeholder="0 1 2 3 ..."/>
                </div>
                <div>
                    <label>Y</label>
                    <input type="text" name="Y" size="30" placeholder="0 1 2 3 ..."/>
                </div>

                <div>
                    <label>k</label>
                    <input type="text" name="k" size="10" placeholder="64"/>
                </div>
                <div>
                    <label>n</label>
                    <input type="text" name="n" size="10" placeholder="100"/>
                </div>

                <div>
                    <label>aX</label>
                    <input type="text" name="aX" size="10" placeholder="3141592653"/>
                </div>
                <div>
                    <label>cX</label>
                    <input type="text" name="cX" size="10" placeholder="2718281829"/>
                </div>
                <div>
                    <label>mX</label>
                    <input type="text" name="mX" size="10" placeholder="35"/>
                </div>
                <div>                
                    <label>seedX</label>
                    <input type="text" name="seedX" size="10" placeholder="5772156649"/>
                </div>

                <div>
                    <label>aY</label>
                    <input type="text" name="aY" size="10" placeholder="2718281829"/>
                </div>
                <div>
                    <label>cY</label>
                    <input type="text" name="cY" size="10" placeholder="3141592653"/>
                </div>
                <div>
                    <label>mY</label>
                    <input type="text" name="mY" size="10" placeholder="35"/>
                </div>
                <div>                
                    <label>seedY</label>
                    <input type="text" name="seedY" size="10" placeholder="1781072418"/>
                </div>
            `;
            form.find("#formContent").html(formContent)

            break;

        case "BD":
            nav.find('ul>li').eq(3).addClass('selected');
            
            var infoContent = `
                <h1>Generator Bays-Durham</h1>
                <p>Opis alg. generatora, jego parametry, origin story itd.</p>
                <p>${lorem_ipsum_txt}</p>`;
            secInfo.html(infoContent)

            var formContent = `

                <div>
                    <label>X</label>
                    <input type="text" name="X" size="30" placeholder="0 1 2 3 ..."/>
                </div>

                <div>
                    <label>k</label>
                    <input type="text" name="k" size="10" placeholder="64"/>
                </div>
                <div>
                    <label>n</label>
                    <input type="text" name="n" size="10" placeholder="100"/>
                </div>

                <div>
                    <label>aX</label>
                    <input type="text" name="aX" size="10" placeholder="3141592653"/>
                </div>
                <div>
                    <label>cX</label>
                    <input type="text" name="cX" size="10" placeholder="2718281829"/>
                </div>
                <div>
                    <label>mX</label>
                    <input type="text" name="mX" size="10" placeholder="35"/>
                </div>
                <div>                
                    <label>seedX</label>
                    <input type="text" name="seedX" size="10" placeholder="5772156649"/>
                </div>
            `;
            form.find("#formContent").html(formContent)

            break;
        
        case "WELL":
            nav.find('ul>li').eq(4).addClass('selected');

            var infoContent = `
                <h1>Generator WELL512a</h1>
                <p>Opis alg. generatora, jego parametry, origin story itd.</p>
                <p>${lorem_ipsum_txt}</p>`;
            secInfo.html(infoContent)

            var formContent = `
                <div>
                    <label>seed</label>
                    <input type="text" name="seed" size="30" placeholder="0 1 2 3 ..."/>
                </div>
                <div>
                    <label>size</label>
                    <input type="text" name="size" size="10" placeholder="100"/>
                </div>
            `;
            form.find("#formContent").html(formContent)

            break;
    }

}

nav.find('ul>li').on('click', function () {
    fillContent($(this).text());
});

fillContent(nav.find('ul>li').eq(0).text())
(function ($) {
    // This function is only responsible for the function of one carousel image each time it is called
    // That is to say, only one carousel will be generated, and the scope of this function can only be assigned to one carousel
    // It is required to pass the root label of the current carousel when calling this function
    // The formal parameter ele here is the root label of a carousel
    var slide = function (ele, options) {
        var $ele = $(ele);
        // default setting options

        var setting = {
            // Control the animation time of the carousel
            speed: 1000,
            // Control the interval time (carousel speed)
            interval: 2000,

        };
        // object merge

        $.extend(true, setting, options);
        // Specify the position and state of each picture
        var states = [
            { $zIndex: 1, width: 470, height: 150, top: 69, left: 134, $opacity: 0.2 },
            { $zIndex: 2, width: 480, height: 170, top: 59, left: 0, $opacity: 0.4 },
            { $zIndex: 3, width: 520, height: 218, top: 35, left: 110, $opacity: 0.7 },
            { $zIndex: 4, width: 574, height: 288, top: 0, left: 263, $opacity: 1 },
            { $zIndex: 3, width: 520, height: 218, top: 35, left: 470, $opacity: 0.7 },
            { $zIndex: 2, width: 480, height: 170, top: 59, left: 620, $opacity: 0.4 },
            { $zIndex: 1, width: 470, height: 150, top: 69, left: 500, $opacity: 0.2 }
        ];

        var $lis = $ele.find('li');
        var timer = null;

        // event
        $ele.find('.Top-next').on('click', function () {
            next();
        });
        $ele.find('.Top-prev').on('click', function () {
            states.push(states.shift());
            move();
        });
        $ele.on('mouseenter', function () {
            clearInterval(timer);
            timer = null;
        }).on('mouseleave', function () {
            autoPlay();
        });

        move();
        autoPlay();

        // Let each li correspond to each state of the above states
        // Let li expand from the middle
        function move() {
            $lis.each(function (index, element) {
                var state = states[index];
                $(element).css('zIndex', state.$zIndex).finish().animate(state, setting.speed).find('img').css('opacity', state.$opacity);
            });
        }

        // switch to the next one
        function next() {
            // Principle: Move the last element of the array to the first
            states.unshift(states.pop());
            move();
        }

        function autoPlay() {
            timer = setInterval(next, setting.interval);
        }
    }
    // Find the root tag of the carousel to be rotated, call slide()
    $.fn.hiSlide = function (options) {
        $(this).each(function (index, ele) {
            slide(ele, options);
        });
        // return value to support chain calls
        return this;
    }
})(jQuery);

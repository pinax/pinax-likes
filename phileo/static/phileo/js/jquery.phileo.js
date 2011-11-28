jQuery(function($) {

    var PhileoLikes = function(form, options) {
        this.options = $.extend({}, $.fn.phileo.defaults, options);
        this.$form = $(form);

        this.$count = $(this.options.count);

        var self = this;
        this.$form.submit(function(event) {
            event.preventDefault();

            $.ajax({
                url: self.$form.attr('action'),
                type: "POST",
                data: self.$form.serialize(),
                statusCode: {
                    200: function(data, textStatus, jqXHR) {
                        self.$count.text(data.likes_count);
                        self.$form[data.liked ? 'addClass' : 'removeClass'](self.options.toggle_class);
                    }
                }
            });
        });
    };

    $.fn.phileo = function(options) {
        $(this).each(function(i, el) {
            var phileo = new PhileoLikes(el, options);
            $(el).data('Phileo', {instance: phileo});
        });
        return this;
    };

    $.fn.phileo.defaults = {
        toggle_class: 'phileo-liked',
        count: false
    };
});

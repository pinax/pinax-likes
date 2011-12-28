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
                        self.$form[data.liked ? 'addClass' : 'removeClass'](self.options.toggle_class);
                        var submit = self.$form.find("input[type=submit]");
                        submit.val(data.liked ? submit.attr("data-unlike-text") : submit.attr("data-like-text"));
                        var count_text = (data.likes_count > 1 || data.likes_count == 0) ? self.$count.attr("data-counts-text-plural") : self.$count.attr("data-counts-text")
                        self.$count.text(data.likes_count + " " + count_text);
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

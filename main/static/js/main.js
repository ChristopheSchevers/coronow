class NavTabs {
    constructor($el) {
        this.$el = $el;
        this.triggers = this.$el.find('[data-target]');
        this.triggers.each(function(){
            return new NavTabItem(this.$el, $(this));
        });
    }
}

class NavTabItem {
    constructor($parent, $el) {
        this.$parent = $parent;
        this.$el = $el;

        this.$el.on('click', { that: this }, this.clickHandler);
    }

    clickHandler(e) {
        const that = e.data.that;
        const id = that.$el.data('target'),
            target = $('[data-tab="' + id + '"]');
        
        if(!target.hasClass('tab-content--open')) {
            $('.tab-content--open').removeClass('tab-content--open');
            target.addClass('tab-content--open');
        }
    }
}

const navtabs = new NavTabs($('[data-navtabs]'));
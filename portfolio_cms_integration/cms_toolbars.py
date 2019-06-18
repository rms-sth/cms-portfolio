from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.utils.urlutils import admin_reverse
from portfolio_app.models import Portfolio


class PortfolioToolbar(CMSToolbar):

	supported_apps = ['portfolio']

	def populate(self):

		if not self.is_current_app:
			return

		#Menus
		menu = self.toolbar.get_or_create_menu(
			'portfolio_cms_integration-portfolio',  # a unique key for this menu
            'Portfolio',                        # the text that should appear in the menu
			)

		menu.add_sideframe_item(
			name='Portfolio list',  # name of the new menu item
			url=admin_reverse('portfolio_app_portfolio_changelist'),  # the URL it should open with
		)

		menu.add_modal_item(
			name='Add a new portfolio',  # name of the new menu item
			url=admin_reverse('portfolio_app_portfolio_add'),  # the URL it should open with
		)

		#Buttons
		buttonlist = self.toolbar.add_button_list()

		buttonlist.add_sideframe_button(
			name='Portfolio list',
			url=admin_reverse('portfolio_app_portfolio_changelist'),
		)

		buttonlist.add_modal_button(
		name = 'Add a new portfolio',
		url = admin_reverse('portfolio_app_portfolio_add'),
		)


# register the toolbar
toolbar_pool.register(PortfolioToolbar)
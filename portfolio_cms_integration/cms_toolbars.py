from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.utils.urlutils import admin_reverse
from portfolio_app.models import Portfolio


class PortfolioToolbar(CMSToolbar):

	supported_apps = ['portfolio']

	def populate(self):

		if not self.is_current_app:
			return

		#Menus Portfolio
		menu = self.toolbar.get_or_create_menu(
			'portfolio_cms_integration-portfolio',  # a unique key for this menu
            'Portfolio',                        # the text that should appear in the menu
		)

		menu.add_sideframe_item(
			name='Portfolio list',  # name of the new menu item
			url=admin_reverse('portfolio_app_portfolio_changelist'),  # the URL it should open with appname_model_name_changelist
		)

		menu.add_modal_item(
			name='Add a new portfolio',  # name of the new menu item
			url=admin_reverse('portfolio_app_portfolio_add'),  # the URL it should open with
		)

		#Buttons Portfolio
		buttonlist = self.toolbar.add_button_list()

		buttonlist.add_sideframe_button(
			name='Portfolio list',
			url=admin_reverse('portfolio_app_portfolio_changelist'),
		)

		buttonlist.add_modal_button(
		name = 'Add a new portfolio',
		url = admin_reverse('portfolio_app_portfolio_add'),
		)

		# Menus Project
		project = self.toolbar.get_or_create_menu(
			'portfolio_cms_integration-project',  # a unique key for this menu
			'Project',  # the text that should appear in the menu
		)

		project.add_modal_item(
			name='Project list',  # name of the new menu item
			url=admin_reverse('portfolio_app_project_changelist'),  # the URL it should open with appname_model_name_changelist
		)

		project.add_modal_item(
			name='Add a new Project',  # name of the new menu item
			url=admin_reverse('portfolio_app_project_add'),  # the URL it should open with
		)

		# Menus Blog
		blog = self.toolbar.get_or_create_menu(
			'portfolio_cms_integration-blog',  # a unique key for this menu
			'Blog',  # the text that should appear in the menu
		)

		blog.add_modal_item(
			name='Blog list',  # name of the new menu item
			url=admin_reverse('portfolio_app_blog_changelist'),  # the URL it should open with appname_model_name_changelist
		)

		blog.add_modal_item(
			name='Add a new Blog',  # name of the new menu item
			url=admin_reverse('portfolio_app_blog_add'),  # the URL it should open with
		)


# register the toolbar
toolbar_pool.register(PortfolioToolbar)
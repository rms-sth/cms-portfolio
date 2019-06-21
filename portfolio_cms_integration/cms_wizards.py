from cms.wizards.wizard_base import Wizard
from cms.wizards.wizard_pool import wizard_pool

from portfolio_cms_integration.forms import PortfolioWizardForm, ProjectoWizardForm


class PortfolioWizard(Wizard):
    pass


class ProjectWizard(Wizard):
    pass

portfolio_wizard = PortfolioWizard(
    title="Create Portfolio",
    weight=200,  # determines the ordering of wizards in the Create dialog
    form=PortfolioWizardForm,
    description="Create a new Portfolio",
)

project_wizard = ProjectWizard(
    title="Create Project",
    weight=200,  # determines the ordering of wizards in the Create dialog
    form=ProjectoWizardForm,
    description="Create a new Project",
)

wizard_pool.register(portfolio_wizard)
wizard_pool.register(project_wizard)
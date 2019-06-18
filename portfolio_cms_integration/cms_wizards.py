from cms.wizards.wizard_base import Wizard
from cms.wizards.wizard_pool import wizard_pool

from portfolio_cms_integration.forms import PortfolioWizardForm


class PortfolioWizard(Wizard):
    pass

portfolio_wizard = PortfolioWizard(
    title="Create Portfolio",
    weight=200,  # determines the ordering of wizards in the Create dialog
    form=PortfolioWizardForm,
    description="Create a new Poll",
)

wizard_pool.register(portfolio_wizard)
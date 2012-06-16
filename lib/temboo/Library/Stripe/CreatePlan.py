
###############################################################################
#
# CreatePlan
# Creates a subscription plan
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreatePlan(Choreography):

    """
    Create a new instance of the CreatePlan Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Stripe/CreatePlan')


    def new_input_set(self):
        return CreatePlanInputSet()

    def _make_result_set(self, result, path):
        return CreatePlanResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreatePlanChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreatePlan
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreatePlanInputSet(InputSet):
        """
        Set the value of the APISecretKey input for this choreography. ((string) The secret API Key providied by Stripe)
        """
        def set_APISecretKey(self, value):
            InputSet._set_input(self, 'APISecretKey', value)

        """
        Set the value of the Amount input for this choreography. ((integer) The amount in cents to charge on a recurring basis for subscribers of this plan)
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the Currency input for this choreography. ((optional, string) 3-letter ISO code for currency. Defaults to 'usd' which is currently the only supported currency.)
        """
        def set_Currency(self, value):
            InputSet._set_input(self, 'Currency', value)

        """
        Set the value of the Interval input for this choreography. ((string) Indicates billing frequency. Valid values are: month or year.)
        """
        def set_Interval(self, value):
            InputSet._set_input(self, 'Interval', value)

        """
        Set the value of the PlanId input for this choreography. ((string) The unique identifier of the plan you want to create)
        """
        def set_PlanId(self, value):
            InputSet._set_input(self, 'PlanId', value)

        """
        Set the value of the PlanName input for this choreography. ((string) The name of the plan which will be displayed in the Stripe web interface.)
        """
        def set_PlanName(self, value):
            InputSet._set_input(self, 'PlanName', value)

        """
        Set the value of the TrialPeriodDays input for this choreography. ((optional, integer) The number of days in a trial period (customer will not be billed until the trial period is over))
        """
        def set_TrialPeriodDays(self, value):
            InputSet._set_input(self, 'TrialPeriodDays', value)


"""
A ResultSet with methods tailored to the values returned by the CreatePlan choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreatePlanResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Stripe)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreatePlanChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreatePlanResultSet(response, path)

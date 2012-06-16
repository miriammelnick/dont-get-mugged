
###############################################################################
#
# ListAllCharges
# Returns a list of all charges or a list of charges for a specified customer.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListAllCharges(Choreography):

    """
    Create a new instance of the ListAllCharges Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Stripe/ListAllCharges')


    def new_input_set(self):
        return ListAllChargesInputSet()

    def _make_result_set(self, result, path):
        return ListAllChargesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllChargesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListAllCharges
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListAllChargesInputSet(InputSet):
        """
        Set the value of the APISecretKey input for this choreography. ((string) The secret API Key providied by Stripe)
        """
        def set_APISecretKey(self, value):
            InputSet._set_input(self, 'APISecretKey', value)

        """
        Set the value of the Count input for this choreography. ((optional, integer) The limit of charges to be returned. Can range from 1 to 100. Defaults to 10.)
        """
        def set_Count(self, value):
            InputSet._set_input(self, 'Count', value)

        """
        Set the value of the CustomerId input for this choreography. ((optional, string) The unique identifier of the customer whose charges to return. If not specified, all charges will be returned.)
        """
        def set_CustomerId(self, value):
            InputSet._set_input(self, 'CustomerId', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) Stripe will return a list of charges starting at the specified offset. Defaults to 0.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)


"""
A ResultSet with methods tailored to the values returned by the ListAllCharges choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListAllChargesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Stripe)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListAllChargesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListAllChargesResultSet(response, path)

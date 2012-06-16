
###############################################################################
#
# PriorityMailServiceRequest
# Request USPS Priority Mail shipping information for a given origin and destination.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PriorityMailServiceRequest(Choreography):

    """
    Create a new instance of the PriorityMailServiceRequest Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/USPS/DeliveryInformationAPI/PriorityMailServiceRequest')


    def new_input_set(self):
        return PriorityMailServiceRequestInputSet()

    def _make_result_set(self, result, path):
        return PriorityMailServiceRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PriorityMailServiceRequestChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PriorityMailServiceRequest
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PriorityMailServiceRequestInputSet(InputSet):
        """
        Set the value of the DestinationZip input for this choreography. ((integer) First 3 digits of a 5-digit zip code)
        """
        def set_DestinationZip(self, value):
            InputSet._set_input(self, 'DestinationZip', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) If you are accessing the production server, set to 'production'. Defaults to 'testing' which indicates that you are using the sandbox.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the OriginZip input for this choreography. ((integer) First 3 digits of a 5-digit zip code)
        """
        def set_OriginZip(self, value):
            InputSet._set_input(self, 'OriginZip', value)

        """
        Set the value of the Password input for this choreography. ((string) The password assigned by USPS)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the UserId input for this choreography. ((string) Alphanumeric ID assigned by USPS.  Required value.)
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the PriorityMailServiceRequest choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PriorityMailServiceRequestResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from USPS Web Service)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PriorityMailServiceRequestChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PriorityMailServiceRequestResultSet(response, path)


###############################################################################
#
# ExpressMailServiceRequest
# Request USPS Express Mail shipping information for a given origin and destination.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ExpressMailServiceRequest(Choreography):

    """
    Create a new instance of the ExpressMailServiceRequest Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/USPS/DeliveryInformationAPI/ExpressMailServiceRequest')


    def new_input_set(self):
        return ExpressMailServiceRequestInputSet()

    def _make_result_set(self, result, path):
        return ExpressMailServiceRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ExpressMailServiceRequestChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ExpressMailServiceRequest
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ExpressMailServiceRequestInputSet(InputSet):
        """
        Set the value of the Date input for this choreography. ((date) Date the package is to be shipped. Must take the form 'MM/DD/YYYY'. )
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the DestinationZip input for this choreography. ((integer) Five digit zip code.)
        """
        def set_DestinationZip(self, value):
            InputSet._set_input(self, 'DestinationZip', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) If you are accessing the production server, set to 'production'. Defaults to 'testing' which indicates that you are using the sandbox.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the OriginZip input for this choreography. ((integer) Three or five digit zip code.)
        """
        def set_OriginZip(self, value):
            InputSet._set_input(self, 'OriginZip', value)

        """
        Set the value of the Password input for this choreography. ((string) The password assigned by USPS)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the UserId input for this choreography. ((string) Alphanumeric ID assigned by USPS)
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the ExpressMailServiceRequest choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ExpressMailServiceRequestResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from USPS Web Service)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ExpressMailServiceRequestChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ExpressMailServiceRequestResultSet(response, path)

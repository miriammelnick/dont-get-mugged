
###############################################################################
#
# TrackingRequest
# Retrieves package information for a specified tracking number.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TrackingRequest(Choreography):

    """
    Create a new instance of the TrackingRequest Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FedEx/TrackingRequest')


    def new_input_set(self):
        return TrackingRequestInputSet()

    def _make_result_set(self, result, path):
        return TrackingRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TrackingRequestChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TrackingRequest
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TrackingRequestInputSet(InputSet):
        """
        Set the value of the AccountNumber input for this choreography. ((required, string) Your FedEx Account Number)
        """
        def set_AccountNumber(self, value):
            InputSet._set_input(self, 'AccountNumber', value)

        """
        Set the value of the AuthenticationKey input for this choreography. ((required, string) The Production Authentication Key provided by FedEx Web Services)
        """
        def set_AuthenticationKey(self, value):
            InputSet._set_input(self, 'AuthenticationKey', value)

        """
        Set the value of the MeterNumber input for this choreography. ((required, string) The Production Meter Number provided by FedEx Web Services)
        """
        def set_MeterNumber(self, value):
            InputSet._set_input(self, 'MeterNumber', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The Production Password provided by FedEx Web Services)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the TrackingNumber input for this choreography. ((required, string) The package tracking number to use in the request)
        """
        def set_TrackingNumber(self, value):
            InputSet._set_input(self, 'TrackingNumber', value)


"""
A ResultSet with methods tailored to the values returned by the TrackingRequest choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TrackingRequestResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from FedEx)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "StatusDescription" output from this choreography execution. ((string) The status description for the package which is parsed from the FedEx response)
        """
        def get_StatusDescription(self):
            return self._output.get('StatusDescription', None)

class TrackingRequestChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TrackingRequestResultSet(response, path)

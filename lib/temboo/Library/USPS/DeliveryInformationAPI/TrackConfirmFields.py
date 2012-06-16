
###############################################################################
#
# TrackConfirmFields
# Track a package sent via USPS and return tracking information with details in separate XML tags.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TrackConfirmFields(Choreography):

    """
    Create a new instance of the TrackConfirmFields Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/USPS/DeliveryInformationAPI/TrackConfirmFields')


    def new_input_set(self):
        return TrackConfirmFieldsInputSet()

    def _make_result_set(self, result, path):
        return TrackConfirmFieldsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TrackConfirmFieldsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TrackConfirmFields
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TrackConfirmFieldsInputSet(InputSet):
        """
        Set the value of the Endpoint input for this choreography. ((optional, string) If you are accessing the production server, set to 'production'. Defaults to 'testing' which indicates that you are using the sandbox.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the Password input for this choreography. ((string) The password assigned by USPS)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the TrackID input for this choreography. ((string) The tracking number.  Can be alphanumeric characters.)
        """
        def set_TrackID(self, value):
            InputSet._set_input(self, 'TrackID', value)

        """
        Set the value of the UserId input for this choreography. ((string) Alphanumeric ID assigned by USPS)
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the TrackConfirmFields choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TrackConfirmFieldsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from USPS Web Service)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class TrackConfirmFieldsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TrackConfirmFieldsResultSet(response, path)

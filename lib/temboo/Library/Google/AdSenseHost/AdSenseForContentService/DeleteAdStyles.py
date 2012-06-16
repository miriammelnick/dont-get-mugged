
###############################################################################
#
# DeleteAdStyles
# Delete a collection of named ad styles from this service.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteAdStyles(Choreography):

    """
    Create a new instance of the DeleteAdStyles Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/AdSenseHost/AdSenseForContentService/DeleteAdStyles')


    def new_input_set(self):
        return DeleteAdStylesInputSet()

    def _make_result_set(self, result, path):
        return DeleteAdStylesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteAdStylesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteAdStyles
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteAdStylesInputSet(InputSet):
        """
        Set the value of the AdStyleNames input for this choreography. ((string) A comma-separated list of ad styles to delete.)
        """
        def set_AdStyleNames(self, value):
            InputSet._set_input(self, 'AdStyleNames', value)

        """
        Set the value of the ClientID input for this choreography. ((string) The ID of the publisher from whom this ad style will be deleted.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the Email input for this choreography. ((string) The developer's email address.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) One of either 'sandbox.google.com' (for testing) or 'www.google.com'. Defaults to 'sandbox.google.com'.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the Password input for this choreography. ((string) The developer's password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the SynServiceID input for this choreography. ((string) The ID for this publisher's AFC syndication service. May be identical to the ClientID.)
        """
        def set_SynServiceID(self, value):
            InputSet._set_input(self, 'SynServiceID', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteAdStyles choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteAdStylesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ()
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteAdStylesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteAdStylesResultSet(response, path)

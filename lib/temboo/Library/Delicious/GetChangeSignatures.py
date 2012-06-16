
###############################################################################
#
# GetChangeSignatures
# Retrieves a list of all bookmarks' change detection signatures.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetChangeSignatures(Choreography):

    """
    Create a new instance of the GetChangeSignatures Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Delicious/GetChangeSignatures')


    def new_input_set(self):
        return GetChangeSignaturesInputSet()

    def _make_result_set(self, result, path):
        return GetChangeSignaturesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetChangeSignaturesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetChangeSignatures
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetChangeSignaturesInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((string) The password that corresponds to the specified Delicious account username.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((string) A valid Delicious account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the GetChangeSignatures choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetChangeSignaturesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response returned from Delicious.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetChangeSignaturesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetChangeSignaturesResultSet(response, path)


###############################################################################
#
# ToggleProperties
# Toggle settings for a document or file on or off, depending on its current state.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ToggleProperties(Choreography):

    """
    Create a new instance of the ToggleProperties Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/ToggleProperties')


    def new_input_set(self):
        return TogglePropertiesInputSet()

    def _make_result_set(self, result, path):
        return TogglePropertiesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TogglePropertiesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ToggleProperties
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TogglePropertiesInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((required, string) Your Google account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Title input for this choreography. ((required, string) The title of the document with the properties you want to toggle. Enclose in quotation marks for an exact, non-case-sensitive match.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the ToggleProperties choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TogglePropertiesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from the Google Documents API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "EditLink" output from this choreography execution. ((string) The edit link URL for the document, parsed from the Google response.)
        """
        def get_EditLink(self):
            return self._output.get('EditLink', None)

class TogglePropertiesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TogglePropertiesResultSet(response, path)

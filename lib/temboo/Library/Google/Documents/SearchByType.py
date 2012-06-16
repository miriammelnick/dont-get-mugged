
###############################################################################
#
# SearchByType
# Retrieves a list of all files of a MIME type you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchByType(Choreography):

    """
    Create a new instance of the SearchByType Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/SearchByType')


    def new_input_set(self):
        return SearchByTypeInputSet()

    def _make_result_set(self, result, path):
        return SearchByTypeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByTypeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchByType
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchByTypeInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((required, string) Your Google account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Type input for this choreography. ((required, string) The MIME type of the files to list: word, excel, powerpoint, pdf, csv, rtf, html, css, xml, plaintext, zip, jpg, or png.)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the SearchByType choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchByTypeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from the Google Documents API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchByTypeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByTypeResultSet(response, path)


###############################################################################
#
# SearchByTitle
# Retrieves information for a file with the title you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchByTitle(Choreography):

    """
    Create a new instance of the SearchByTitle Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/SearchByTitle')


    def new_input_set(self):
        return SearchByTitleInputSet()

    def _make_result_set(self, result, path):
        return SearchByTitleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByTitleChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchByTitle
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchByTitleInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((required, string) Your Google account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Title input for this choreography. ((required, string) The title of the document to search for. Enclose in quotation marks for an exact, non-case-sensitive match.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the SearchByTitle choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchByTitleResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from the Google Documents API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "EditMediaLink" output from this choreography execution. ((string) The 'resumable-edit-media' link of the document. This link is used when editing the content of an existing Google doc.)
        """
        def get_EditMediaLink(self):
            return self._output.get('EditMediaLink', None)
        """
        Retrieve the value for the "EditMetaDataLink" output from this choreography execution. ((string) The 'edit' link of the document. This link is used when editing the metadata of an existing Google doc.)
        """
        def get_EditMetaDataLink(self):
            return self._output.get('EditMetaDataLink', None)
        """
        Retrieve the value for the "ResourceID" output from this choreography execution. ((string) The document resource ID returned from Google.)
        """
        def get_ResourceID(self):
            return self._output.get('ResourceID', None)

class SearchByTitleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByTitleResultSet(response, path)

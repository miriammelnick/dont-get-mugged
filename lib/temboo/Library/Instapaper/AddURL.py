
###############################################################################
#
# AddURL
# Add a document to an Instapaper account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddURL(Choreography):

    """
    Create a new instance of the AddURL Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Instapaper/AddURL')


    def new_input_set(self):
        return AddURLInputSet()

    def _make_result_set(self, result, path):
        return AddURLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddURLChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddURL
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddURLInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((required, string) Enter an Instapaper password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Selection input for this choreography. ((optional, string) Enter a description of the URL being added.)
        """
        def set_Selection(self, value):
            InputSet._set_input(self, 'Selection', value)

        """
        Set the value of the Title input for this choreography. ((optional, string) Enter a titile for the uploaded URL. If no title is provided, Instapaper will crawl the URL to detect a title.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the URL input for this choreography. ((required, string) Enter the URL of the document that is being added to an Instapaper account.)
        """
        def set_URL(self, value):
            InputSet._set_input(self, 'URL', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Enter an Instapaper username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the AddURL choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddURLResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((integer) The response from Instapaper. Successful reqests will return a 201 status code.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AddURLChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddURLResultSet(response, path)

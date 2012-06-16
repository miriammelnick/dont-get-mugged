
###############################################################################
#
# ListMembers
# Retrieves the email addresses of members of a MailChimp list. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListMembers(Choreography):

    """
    Create a new instance of the ListMembers Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/ListMembers')


    def new_input_set(self):
        return ListMembersInputSet()

    def _make_result_set(self, result, path):
        return ListMembersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListMembersChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListMembers
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListMembersInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Mailchimp.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Specifies the number of records in a page to be returned. Must be greater than zero and less than or equal to 15000. Defaults to 100.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the ListId input for this choreography. ((required, string) The id of the Mailchimp list to retrieve members from.)
        """
        def set_ListId(self, value):
            InputSet._set_input(self, 'ListId', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Indicates the desired format for the response. Accepted values are "json" or "xml" (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Since input for this choreography. ((optional, date) Retrieves records that have changed since this date/time. Formatted like 'YYYY-MM-DD HH:MM:SS.)
        """
        def set_Since(self, value):
            InputSet._set_input(self, 'Since', value)

        """
        Set the value of the Start input for this choreography. ((optional, integer) Specifies the page at which to begin returning records. Page size is defined by the limit argument. Must be zero or greater. Defaults to 0.)
        """
        def set_Start(self, value):
            InputSet._set_input(self, 'Start', value)

        """
        Set the value of the Status input for this choreography. ((optional, string) Must be one of 'subscribed', 'unsubscribed', 'cleaned', or 'updated'. Defaults to 'subscribed'.)
        """
        def set_Status(self, value):
            InputSet._set_input(self, 'Status', value)


"""
A ResultSet with methods tailored to the values returned by the ListMembers choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListMembersResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Mailchimp. Corresponds to the format specified in the Output parameter. Defaults to "xml".)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListMembersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListMembersResultSet(response, path)

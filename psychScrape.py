import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
from time import sleep
from tqdm import tqdm

terms = ['Intellectual Disability', 'Intellectual Developmental Disorder', 'Global Developmental Delay', 'Language Disorder',
         'Speech Sound Disorder', 'Phonological Disorder', 'Childhood-Onset Fluency Disorder', 'Stuttering', 'Social Communication Disorder',
         'Autism Spectrum Disorder', 'Attention-Deficit/Hyperactivity Disorder', 'Tourette’s Disorder', 'Motor Tic Disorder',
         'Vocal Tic Disorder', 'Neurodevelopmental Disorder', 'Schizotypal Personality Disorder', 'Delusional Disorder',
         'Brief Psychotic Disorder', 'Schizophreniform Disorder', 'Schizophrenia', 'Schizoaffective Disorder',
         'Substance-Induced Psychotic Disorder', 'Medication-Induced Psychotic Disorder', 'Catatonia', 'Bipolar I Disorder',
         'Bipolar II Disorder', 'Cyclothymic Disorder', 'Disruptive Mood Dysregulation Disorder', 'Major Depressive Disorder',
         'Persistent Depressive Disorder', 'Premenstrual Dysphoric Disorder', 'Dysthymia',
         'Substance or Medication-Induced Depressive Disorder', 'Depressive Disorder Due to Another Medical Condition', 'Depression',
         'Separation Anxiety Disorder', 'Selective Mutism', 'Specific Phobia', 'Social Anxiety Disorder', 'Social phobia', 'Panic Disorder',
         'Panic Attack', 'Agoraphobia', 'Generalized Anxiety Disorder', 'Substance-Induced Anxiety Disorder',
         'Medication-Induced Anxiety Disorder', 'Anxiety', 'Obsessive-Compulsive Disorder', 'Body Dysmorphic Disorder',
         'Hoarding Disorder', 'Trichotillomania', 'Hair-Pulling Disorder', 'Excoriation', 'Skin-Picking', 'Reactive Attachment Disorder',
         'Disinhibited Social Engagement Disorder', 'Posttraumatic Stress Disorder', 'Acute Stress Disorder', 'Adjustment Disorders',
         'Dissociative Identity Disorder', 'Dissociative Amnesia', 'Depersonalization/Derealization Disorder', 'Somatic Symptom Disorder',
         'Illness Anxiety Disorder', 'Conversion Disorder', 'Functional Neurological Symptom Disorder', 'Factitious Disorder', 'Pica',
         'Rumination Disorder', 'Avoidant/Restrictive Food Intake Disorder', 'Anorexia Nervosa', 'Enuresis', 'Encopresis',
         'Insomnia Disorder', 'Hypersomnolence Disorder', 'Narcolepsy', 'Obstructive Sleep Apnea', 'Hypopnea', 'Central Sleep Apnea',
         'Sleep-Related Hypoventilation', 'Sleepwalking', 'Sleep Terrors', 'Nightmare Disorder',
         'Rapid Eye Movement Sleep Behavior Disorder', 'Restless Legs Syndrome', 'Delayed Ejaculation', 'Erectile Disorder',
         'Female Orgasmic Disorder', 'Female Sexual Interest/Arousal Disorder', 'Genito-Pelvic Pain/Penetration Disorder',
         'Premature Ejaculation', 'Gender Dysphoria', 'Oppositional Defiant Disorder', 'Intermittent Explosive Disorder',
         'Conduct Disorder', 'Antisocial Personality Disorder', 'Pyromania', 'Kleptomania', 'Alcohol Use Disorder', 'Alcohol Intoxication',
         'Alcohol Withdrawal', 'Caffeine Intoxication', 'Caffeine Withdrawal', 'Cannabis Use Disorder', 'Cannabis Intoxication',
         'Cannabis Withdrawal', 'Phencyclidine Use Disorder', 'Inhalant Use Disorder', 'Inhalant Intoxication', 'Opioid Use Disorder',
         'Opioid Intoxication', 'Opioid Withdrawal', 'Stimulant Use Disorder', 'Stimulant Intoxication', 'Stimulant Withdrawal',
         'Tobacco Use Disorder', 'Tobacco Withdrawal', 'Gambling Disorder', 'Delirium', 'Major Neurocognitive Disorder',
         'Mild Neurocognitive Disorder', 'Alzheimer’s Disease', 'Frontotemporal Dementia', 'Lewy Body Dementia', 'Vascular Dementia',
         'Traumatic Brain Injury', 'TBI', 'Traumatic Brain Injury', 'Paranoid Personality Disorder', 'Schizoid Personality Disorder',
         'Schizotypal Personality Disorder', 'Antisocial Personality Disorder', 'Borderline Personality Disorder',
         'Histrionic Personality Disorder', 'Narcissistic Personality Disorder', 'Avoidant Personality Disorder',
         'Dependent Personality Disorder', 'Obsessive-Compulsive Personality Disorder', 'Voyeuristic Disorder',
         'Exhibitionistic Disorder', 'Frotteuristic Disorder', 'Sexual Masochism Disorder', 'Sexual Sadism Disorder',
         'Pedophilic Disorder', 'Fetishistic Disorder', 'Transvestic Disorder', 'Cognitive Behavioral Therapy (CBT)',
         'Cognitive Distortions', 'Filtering', 'Black and White Thinking', 'All or nothing thinking', 'Polarized Thinking',
         'Overgeneralization', 'Jumping to Conclusions', 'Catastrophizing', 'Personalization', 'Control Fallacies', 'Fallacy of Fairness',
         'Fallacy of Change (CBT)', 'Blaming (CBT)', 'Shoulds (CBT)', 'Emotional Reasoning (CBT)', 'Global Labeling (CBT)', 'Always Being Right (CBT)', 'Heaven’s Reward Fallacy (CBT)', 'Automatic Thoughts (CBT)',
         'Core Beliefs (CBT)']
terms = list(set(terms))

testterms = terms[:10]

terms_list = []
results_list = []

stop_terms = ['Very common', 'Very rare', 'Common', 'COMMON CAUSES', 'Rare', 'Sources:',
              'For informational purposes only. Consult your local medical authority for advice.']

redo_terms = ["Dysthymia", "Conduct Disorder", "Excoriation", "Social Communication Disorder", "Transvestic Disorder",
              "Stimulant Intoxication", "Cannabis Withdrawal", "Rapid Eye Movement Sleep Behavior Disorder",
              "Substance-Induced Anxiety Disorder", "Restless Legs Syndrome", "Autism Spectrum Disorder",
              "Specific Phobia", "Sleepwalking", "Control Fallacies", "Obstructive Sleep Apnea", "Narcolepsy",
              "Frontotemporal Dementia", "Medication-Induced Psychotic Disorder", "Hoarding Disorder",
              "Major Depressive Disorder", "Female Sexual Interest/Arousal Disorder"]

driver = webdriver.Chrome()
driver.get("https://www.google.com")

for term in tqdm(redo_terms):
    sleep(randint(1, 4))
    search_bar = driver.find_element_by_xpath("//input[@name='q']")
    search_bar.clear()
    search_bar.click()
    search_bar.send_keys(term)
    search_bar.send_keys(Keys.RETURN)
    sleep(.5)  # wait for the page to load fully

    contains_result = driver.find_elements_by_xpath(
        "//div[contains(@class, 'PZPZlf')]")
    result_text = ""
    for result in contains_result:
        # Stop using stop words
        if result.text in stop_terms:
            break

        if len(result.text) > 1 and result.text[-1] == "." and result.text[-2] != ".":
            result_text += result.text + " "

    if len(result_text.strip()) > 0:
        print(result_text)
        terms_list.append(term)
        results_list.append(result_text)

final_scrape_df = pd.DataFrame([terms_list, results_list]).transpose()
final_scrape_df.columns = ['term', 'result']
final_scrape_df.to_csv(
    '/Users/jackkeane/AppDev/Jacobson/scrapers/psych_scraper/redo_terms.csv')
